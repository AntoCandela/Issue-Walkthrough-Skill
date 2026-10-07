"""Render annotated HTML figures to PNGs. Requires Playwright and Chromium."""
import argparse
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

LOG = logging.getLogger(__name__)
SKILL = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="Trusted local HTML page with relative assets")
    parser.add_argument("--output", type=Path, help="New export directory; defaults to skill .cache/exports/<run>")
    parser.add_argument("--selector", default=".annotated-shot, figure > a > img", help="Annotated steps and comparison images, in document order")
    parser.add_argument("--width", type=int, default=1440, help="Viewport width in CSS pixels")
    args = parser.parse_args()
    source = args.html.resolve(strict=True)
    if not source.is_file() or args.width < 320:
        parser.error("Supply an HTML file and a viewport width of at least 320.")
    from playwright.sync_api import sync_playwright
    run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid4().hex[:8]
    output = (args.output or SKILL / ".cache" / "exports" / run).resolve()
    output.mkdir(parents=True, exist_ok=False)
    images = output / "images"
    images.mkdir()
    manifest = {"source": str(source), "status": "incomplete", "viewport_width": args.width, "images": []}
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch()
            context = browser.new_context(viewport={"width": args.width, "height": 1000}, device_scale_factor=2, service_workers="block")
            # Local, trusted reports only. Do not fetch remote assets during export.
            context.route("http://**/*", lambda route: route.abort())
            context.route("https://**/*", lambda route: route.abort())
            page = context.new_page()
            page.goto(source.as_uri(), wait_until="load")
            page.evaluate("document.fonts.ready")
            targets = page.locator(args.selector)
            if targets.count() == 0:
                raise ValueError("No matching figures. Check --selector; nothing was exported.")
            for index in range(targets.count()):
                target = targets.nth(index)
                # Comparisons may be inside collapsed details.
                target.evaluate("el => { for (let p = el.parentElement; p; p = p.parentElement) if (p.tagName === 'DETAILS') p.open = true; }")
                metadata = target.evaluate("""async el => {
                    const imgs = el.matches('img') ? [el] : [...el.querySelectorAll('img')];
                    if (!imgs.length) throw new Error('Figure has no screenshot');
                    await Promise.all(imgs.map(img => img.decode()));
                    const svg = el.querySelector('svg');
                    if (svg && imgs.length === 1) {
                        const b = svg.viewBox.baseVal;
                        if (b.width !== imgs[0].naturalWidth || b.height !== imgs[0].naturalHeight)
                            throw new Error('SVG viewBox does not match decoded screenshot dimensions');
                    }
                    return {caption: el.closest('figure')?.querySelector('figcaption')?.innerText || '',
                        sources: imgs.map(img => ({src: img.getAttribute('src'), width: img.naturalWidth, height: img.naturalHeight}))};
                }""")
                filename = f"{index + 1:02d}-figure.png"
                target.screenshot(path=str(images / filename), animations="disabled")
                manifest["images"].append({"file": "images/" + filename, **metadata})
            browser.close()
        manifest["status"] = "rendered; visual review required"
    except Exception as error:
        manifest["error"] = str(error)
        raise
    finally:
        (output / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
        LOG.info("Export folder: %s", output)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main()
