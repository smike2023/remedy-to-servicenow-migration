# Remedy to ServiceNow Migration Survival Kit 🚀

This repository contains tools, documentation, and templates to support a full migration from BMC Remedy (SRXML format) to ServiceNow CMDB and related modules.

---

## 📁 Folder Structure

- `scripts/`  
  Contains Python scripts to parse and transform SRXML, including a starter parser.

- `transform_maps/`  
  Sample ServiceNow transform map configurations in JSON format.

- `import_samples/`  
  Example SRXML files and ServiceNow-compatible XML output for testing imports.

- `docs/`  
  Markdown guides, mapping walkthroughs, and business rule cheat sheets.

- `notion/`  
  A Notion dashboard template to track your migration project in detail.

- `one-pager/`  
  Printable PDF War Map summarizing the ETL flow and migration phases.

---

## 🧠 Project Goals

- Flatten complex SRXML data into ServiceNow-readable format
- Create import set tables and transform maps for automated ingestion
- Empower non-developers with step-by-step documentation
- Maintain operational awareness with a visual War Map and Notion board

---

## 🛠️ Requirements

- Git
- Python 3.x
- Access to ServiceNow instance (with Import Set/Transform Map permissions)

---

## ✅ Getting Started

1. Clone this repository
2. Follow the `docs/TSR_Mapping_Plan.md` for step-by-step import guidance
3. Use `scripts/srxml_parser.py` to test parsing your SRXML files
4. Load results into ServiceNow using your import set + transform map
5. Reference the War Map for your ETL strategy

---

## 🧩 Contribute

PRs and forks welcome — especially if you’ve mapped more SRXML edge cases.

---

## 🔐 Status

This repo is currently under active setup by @SamMike for a federal data migration project.

