#!/usr/bin/env python3
"""Demonstrate core os & os.path operations safely in a sandbox tree."""
import os, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WORK = ROOT / "work"
(WORK / "sub/child").mkdir(parents=True, exist_ok=True)
(WORK / "sub/child/file.txt").write_text("hello\n", encoding="utf-8")

def listdir_and_stat():
    items = os.listdir(WORK)
    print("[listdir]", items)
    for name in items:
        p = WORK / name
        st = os.stat(p)
        print(f"[stat] {{'path': '{p.name}', 'size': {st.st_size}, 'mtime': {int(st.st_mtime)}}}")

def split_dir_base():
    cur = str(WORK / "sub/child")
    print("[split]", os.path.split(cur))
    print("[dirname]", os.path.dirname(cur))
    print("[basename]", os.path.basename(cur))

def find_rc(rc_name=".examplerc"):
    # env var first
    var = "EXAMPLERC_DIR"
    if var in os.environ:
        cfg = os.path.join(os.path.expandvars(f"${{var}}"), rc_name)
        if os.path.exists(cfg):
            return cfg
    # CWD
    cfg = os.path.join(os.getcwd(), rc_name)
    if os.path.exists(cfg): return cfg
    # HOME
    cfg = os.path.join(os.path.expanduser("~"), rc_name)
    if os.path.exists(cfg): return cfg
    # Next to this script
    cfg = os.path.join(os.path.dirname(__file__), rc_name)
    if os.path.exists(cfg): return cfg
    return None

def walk_tree():
    for parent, dirs, files in os.walk(WORK):
        for fn in files:
            p = os.path.join(parent, fn)
            print("[walk]", p, os.path.getsize(p))

if __name__ == "__main__":
    listdir_and_stat()
    split_dir_base()
    print("[find_rc]", find_rc())
    walk_tree()
