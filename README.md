# Remedy to ServiceNow SRXML Migration – Transformation Prototype

This repository documents a mock workflow and proof-of-work framework for converting legacy Remedy SRXML data into ServiceNow-compatible XML for import and transformation.

## 📌 Objective

To demonstrate a working model for the **transform and load** phases of a Remedy to ServiceNow migration, using placeholder data and mocked structure — pending official access to SRXML source files or schema documentation.

## 🧱 Workflow Overview

### Step 1: Extract (Blocked)

- Source data (SRXML exports from Remedy) is assumed to be handled by Dan (Remedy gatekeeper).
- No access has been provided as of this writing.

### Step 2: Transform (Prototype in Progress)

- **Input**: SampleC:\Users\sammy\OneDrive\Documents\@BCMC\projects\RemedySNOWMigration\mock SRXML file (`C:\Users\sammy\OneDrive\Documents\@BCMC\projects\RemedySNOWMigration\samplesC:\Users\sammy\OneDrive\Documents\@BCMC\projects\RemedySNOWMigration\mock_srxml.xml`)
- **Process**: Parse XML → flatten hierarchy → cleanC:\Users\sammy\OneDrive\Documents\@BCMC\projects\RemedySNOWMigration\normalize values
- **Output**: Flattened XML compatible with ServiceNow Import Sets

### Step 3: Load

- Import flattened XML using ServiceNow Import Sets
- Use Transform Maps to map to appropriate target tables (e.g., `cmdb_ci`, `sc_req_item`, etc.)

## 🛠️ Tools & Scripts

- `parse_srxml.py`: Reads SRXML file and prints basic structure (placeholder logic)
- `flatten_srxml.py`: Converts nested XML into flattened keyC:\Users\sammy\OneDrive\Documents\@BCMC\projects\RemedySNOWMigration\value format
- `transform_map_sample.xlsx`: Spreadsheet for defining mappings between SRXML fields and ServiceNow fields

## ✅ Proof of Work

- All work here is based on available public data and placeholder assumptions.
- This repo serves as documentation of initiative taken *prior to receiving official data*.

## 🚫 Known Blockers

| Area         | Status       | Details                                      |
|--------------|--------------|----------------------------------------------|
| SRXML Access | Blocked      | No source files or schema provided yet       |
| SQL Scripts  | Incomplete   | Provided with no context or source mappings  |
| Role Clarity | Misaligned   | Remedy experience was assumed but never scoped |

## 🔒 Context (Internal)

This repo is maintained by a BCMC contractor assigned to assist with data transformation tasks on the DISA Remedy → ServiceNow migration. This repo exists to demonstrate readiness and initiative while awaiting access to source data or clarified scope from project leadership.

## 📁 Directory Structure

```
C:\Users\sammy\OneDrive\Documents\@BCMC\projects\RemedySNOWMigration\
├── samplesC:\Users\sammy\OneDrive\Documents\@BCMC\projects\RemedySNOWMigration\
│   └── mock_srxml.xml
├── scriptsC:\Users\sammy\OneDrive\Documents\@BCMC\projects\RemedySNOWMigration\
│   ├── parse_srxml.py
│   └── flatten_srxml.py
├── transform_map_sample.xlsx
└── README.md
```
