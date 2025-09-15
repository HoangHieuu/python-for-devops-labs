#!/usr/bin/env python3
"""Re-implement path logic with pathlib objects."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent

def find_rc(rc_name=".examplerc"):
    var = os.environ.get("EXAMPLERC_DIR")
    if var:
        p = Path(var) / rc_name
        print("[check]", p)
        if p.exists(): return p.as_posix()
    p = Path.cwd() / rc_name
    print("[check]", p)
    if p.exists(): return p.as_posix()
    p = Path.home() / rc_name
    print("[check]", p)
    if p.exists(): return p.as_posix()
    here = Path(__file__).resolve().parent / rc_name
    print("[check]", here)
    if here.exists(): return here.as_posix()
    return None

def basics():
    print("[cwd]", Path.cwd())
    print("[home]", Path.home())
    sandbox = ROOT / "pathlib_sandbox"
    sandbox.mkdir(exist_ok=True)
    f = sandbox / "hello.txt"
    f.write_text("hi\n", encoding="utf-8")
    print("[exists]", f.exists(), "[text]", f.read_text(encoding="utf-8").strip())

if __name__ == "__main__":
    basics()
    print("[find_rc]", find_rc())
