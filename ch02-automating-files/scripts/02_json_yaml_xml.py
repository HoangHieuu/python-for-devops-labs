#!/usr/bin/env python3
"""Work with JSON (stdlib), YAML (optional), and XML (stdlib)."""
from pathlib import Path
import json, sys
import xml.etree.ElementTree as ET

DATA = Path(__file__).resolve().parent / "data"

def json_demo():
    p = DATA / "service-policy.json"
    policy = json.loads(p.read_text(encoding="utf-8"))
    print("[json_demo] Resource before:", policy["Statement"][0]["Resource"])
    policy["Statement"][0]["Resource"] = "S3"
    p.write_text(json.dumps(policy, indent=2), encoding="utf-8")
    print("[json_demo] Resource after: ", policy["Statement"][0]["Resource"])

def yaml_demo():
    yml = DATA / "verify-apache.yml"
    try:
        import yaml
    except Exception as e:
        print("[yaml_demo] PyYAML not installed. Showing file content only.")
        print(yml.read_text(encoding="utf-8"))
        return
    with yml.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    print("[yaml_demo] top-level type:", type(data).__name__)
    print("[yaml_demo] first task name:", data[0]["tasks"][0]["name"])
    # roundtrip write
    yml_out = DATA / "verify-apache.out.yml"
    with yml_out.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)
    print("[yaml_demo] wrote", yml_out.name)

def xml_demo():
    ns = {"a": "http://www.w3.org/2005/Atom"}
    p = DATA / "feed.atom.xml"
    root = ET.parse(str(p)).getroot()
    authors = root.findall("a:entry/a:author/a:name", ns)
    print("[xml_demo] authors:", ", ".join(a.text for a in authors))

if __name__ == "__main__":
    json_demo()
    yaml_demo()
    xml_demo()
