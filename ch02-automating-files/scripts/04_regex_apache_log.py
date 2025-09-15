#!/usr/bin/env python3
"""Parse Apache CLF log with regex; print IPs for GET on 08/Nov/2019."""
from pathlib import Path
import re

DATA = Path(__file__).resolve().parent / "data"
log_text = (DATA / "access.log").read_text(encoding="utf-8")

# Pattern with named groups
pat = re.compile(
    r'(?P<IP>\d+\.\d+\.\d+\.\d+)\s+-\s+(?P<User>\S+)\s+'
    r'\[(?P<Time>08/Nov/2019:\d{2}:\d{2}:\d{2})(?:\s[+-]\d{4})?\]\s+'
    r'"(?P<Method>GET)\s+(?P<Path>[^"]*)"\s+(?P<Status>\d{3})\s+(?P<Size>\d+)'
)

if __name__ == "__main__":
    for m in pat.finditer(log_text):
        print("[ip]", m.group("IP"), "->", m.group("Path"))
