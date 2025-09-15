#!/usr/bin/env python3
"""Read CSV with csv (stdlib). Optionally demo pandas if available."""
from pathlib import Path
import csv

DATA = Path(__file__).resolve().parent / "data"

def csv_reader_demo():
    p = DATA / "sample-data.csv"
    with p.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            print("[csv]", row)
            if i == 5: break

def pandas_demo():
    try:
        import pandas as pd
    except Exception:
        print("[pandas_demo] pandas not installed; skipping.")
        return
    p = DATA / "sample-data.csv"
    df = pd.read_csv(p)
    print(df.head(3))
    print(df.describe())

if __name__ == "__main__":
    csv_reader_demo()
    pandas_demo()
