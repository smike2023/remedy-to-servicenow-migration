# Remedy to ServiceNow SRXML Migration – Transformation Prototype

This repository documents a mock workflow and proof-of-work framework for converting legacy Remedy SRXML data into ServiceNow-compatible XML for import and transformation.

## 📌 Objective

To demonstrate a working model for the **transform and load** phases of a Remedy to ServiceNow migration, using placeholder data and mocked structure — pending official access to SRXML source files or schema documentation.

## 🧱 Workflow Overview

### Step 1: Extract (Blocked)

- Source data (SRXML exports from Remedy) is assumed to be handled by a restricted access group.
- No access has been provided as of this writing.

### Step 2: Transform (Prototype in Progress)

- **Input**: Sample/mock SRXML file (`mock_srxml.xml`)
- **Process**: Parse XML → flatten hierarchy → clean/normalize values
- **Output**: Flattened XML compatible with ServiceNow Import Sets

### Step 3: Load

- Import flattened XML using ServiceNow Import Sets
- Use Transform Maps to map to appropriate target tables (e.g., `cmdb_ci`, `sc_req_item`, etc.)

## 🛠️ Tools & Scripts

- `scripts/parse_srxml.py`: Reads SRXML file and prints basic structure
- `scripts/flatten_srxml.py`: Converts nested XML into flattened key/value format
- `mock_srxml.xml`: Example Remedy data file for prototyping
- `transform_map_sample.xlsx`: Spreadsheet for mapping SRXML fields to ServiceNow targets

## ✅ Proof of Work

- All work here is based on available public data and placeholder assumptions.
- This repo serves as documentation of initiative taken *prior to receiving official data*.

## 🚫 Known Blockers

| Area         | Status       | Details                                      |
|--------------|--------------|----------------------------------------------|
| SRXML Access | Blocked      | No source files or schema provided yet       |
| SQL Scripts  | Incomplete   | Provided with no context or source mappings  |
| Role Clarity | Misaligned   | Legacy platform expertise was assumed        |

## 🔒 Context

This repo is maintained by a contractor assigned to assist with data transformation tasks on a Remedy → ServiceNow migration. It exists to demonstrate readiness and initiative while awaiting access to source data or clarified scope from project stakeholders.

## 📁 Directory Structure

```
/
├── mock_srxml.xml
├── transform_map_sample.xlsx
├── scripts/
│   ├── parse_srxml.py
│   └── flatten_srxml.py
└── README.md
```
