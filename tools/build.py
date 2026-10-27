"""Rebuild index.html from src/game.src.html by inlining three.js (r128).

Usage (from the repository root):
    npm install three@0.128.0
    python3 tools/build.py
"""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
three = root / "node_modules" / "three"
files = [
    "build/three.min.js",
    "examples/js/shaders/CopyShader.js",
    "examples/js/shaders/LuminosityHighPassShader.js",
    "examples/js/postprocessing/EffectComposer.js",
    "examples/js/postprocessing/RenderPass.js",
    "examples/js/postprocessing/ShaderPass.js",
    "examples/js/postprocessing/UnrealBloomPass.js",
]
libs = "".join(
    "<script>" + (three / f).read_text(encoding="utf8").replace("</script>", "<\\/script>") + "</script>\n"
    for f in files
)
src = (root / "src" / "game.src.html").read_text(encoding="utf8")
(root / "index.html").write_text(src.replace("<!--LIBS-->", libs), encoding="utf8")
print("Built index.html")
