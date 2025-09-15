#!/usr/bin/env python3
"""Chapter 2 – Reading & Writing text/binary safely and portably."""
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"

def read_whole_file():
    p = DATA / "bookofdreams.txt"
    text = p.read_text(encoding="utf-8")
    print("[read_whole_file] length:", len(text))
    print("[read_whole_file] char[56]:", text[56] if len(text) > 56 else "<none>")

def read_by_lines():
    p = DATA / "bookofdreams.txt"
    with p.open("r", encoding="utf-8") as f:
        lines = f.readlines()
    print("[read_by_lines] n_lines:", len(lines))
    print("[read_by_lines] first line:", lines[0].rstrip())

def normalize_eol_copy():
    src = DATA / "bookofdreams.txt"
    dst = DATA / "bookofdreams_copy.txt"
    with src.open("r", encoding="utf-8") as s, dst.open("w", encoding="utf-8", newline="\n") as t:
        for line in s:
            t.write(line)
    print("[normalize_eol_copy] wrote", dst)

def binary_write_read():
    p = DATA / "demo.bin"
    first8 = p.read_bytes()[:8]
    print("[binary_read] first 8 bytes:", first8)

def write_envrc():
    p = DATA / ".envrc"
    print("[write_envrc] exists:", p.exists())
    print(p.read_text(encoding="utf-8"))

def line_reader(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line

def generator_demo():
    src = DATA / "bookofdreams.txt"
    for i, line in enumerate(line_reader(src)):
        if i > 1: break
        print(f"[generator_demo] line {i}:", line.rstrip())

def binary_chunk_read():
    p = DATA / "demo.bin"
    total = 0
    with p.open("rb") as f:
        while True:
            chunk = f.read(32)
            if not chunk: break
            total += len(chunk)
    print("[binary_chunk_read] size via chunks:", total)

if __name__ == "__main__":
    read_whole_file()
    read_by_lines()
    normalize_eol_copy()
    binary_write_read()
    write_envrc()
    generator_demo()
    binary_chunk_read()
