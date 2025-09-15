# Chapter 2 — Automating Files & the Filesystem

Examples and runnable labs inspired by **_Python for DevOps_ – Chapter 2**.  
This folder demonstrates safe, portable file automation in Python: reading/writing text & binary, processing large files, parsing JSON/YAML/XML, searching logs with regex, and working with the OS filesystem via `os`, `os.path`, and `pathlib`.

---

## 🎯 Learning goals

- Read/Write **text** (with UTF-8) and **binary** data safely
- Stream **large files** line-by-line or in **chunks**
- Parse & emit **JSON** (stdlib), **YAML** (PyYAML, optional), **XML** (ElementTree)
- Use **regular expressions** to extract data from logs (Common Log Format)
- Manage paths & metadata with **`os`/`os.path`** and **`pathlib`**
- Implement a robust **“find rc file”** strategy (env → CWD → HOME → alongside script)

---

## 📁 Layout
```bash
ch02-automating-files/
├── README.md
├── requirements-optional.txt
├── scripts/
│ ├── 01_text_files.py # text/binary I/O, newline normalize, generators
│ ├── 02_json_yaml_xml.py # JSON (stdlib), YAML (optional), XML (stdlib)
│ ├── 03_csv_and_pandas.py 
│ ├── 04_regex_apache_log.py 
│ ├── 05_os_and_path.py # os + os.path: listdir/stat/split/os.walk + find_rc
│ └── 06_pathlib_demo.py # pathlib: đường dẫn như object; rewrite find_rc
└── data/
├── bookofdreams.txt # text 
├── demo.bin # binary 
├── .envrc # file env ví dụ
├── service-policy.json # JSON policy
├── verify-apache.yml # YAML (Ansible-like)
├── feed.atom.xml # XML (Atom)
├── sample-data.csv 
└── access.log 


---
```
## ⚙️ Prerequisites

- **Python 3.9+** (Recommend 3.10+)

Using Virtual Environment(Recommended):
```bash
cd ch02-automating-files
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

# Optional dependencies
pip install -r requirements-optional.txt
