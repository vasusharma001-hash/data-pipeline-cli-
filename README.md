# Data Pipeline CLI Tool

A command-line tool for loading, cleaning, inspecting, and exporting structured datasets from local files and REST APIs.


# Problem

Real-world datasets are often messy and difficult to inspect manually.

Common issues include:

- Duplicate records
- Missing values
- Inconsistent data formats
- Multiple input sources (CSV, Excel, APIs)

This project automates common data preparation tasks and generates a clean, structured dataset ready for further analysis.


# Features

- Load CSV files
- Load JSON files
- Load Excel (.xlsx) files
- Load data directly from REST APIs
- Automatically flatten nested JSON responses
- Inspect dataset structure
- Remove duplicate rows
- Remove rows containing missing values
- Display formatted reports using Rich
- Export cleaned datasets
- CLI interface using argparse


# Supported Input Sources

### Local Files

- CSV (.csv)
- JSON (.json)
- Excel (.xlsx)

### REST APIs

Example:

```bash
python main.py --url https://jsonplaceholder.typicode.com/users
```


# Supported Output Formats

- CSV (.csv)
- JSON (.json)
- Excel (.xlsx)


# Project Structure

```text
data-pipeline-cli/

main.py
loader.py
cleaner.py
display.py
export.py

sample_data.csv
sample_data.json
sample_data.xlsx

requirements.txt
README.md
.gitignore
```


# Modules

- **main.py** — Controls the complete pipeline workflow
- **loader.py** — Loads data from files and REST APIs
- **cleaner.py** — Removes duplicates and missing values
- **display.py** — Generates Rich terminal reports
- **export.py** — Exports cleaned datasets


# Installation

```bash
git clone https://github.com/vasusharma001-hash/data-pipeline-cli-.git

cd data-pipeline-cli

pip install -r requirements.txt
```


# Usage

### CSV

```bash
python main.py --file sample_data.csv
```

### JSON

```bash
python main.py --file sample_data.json
```

### Excel

```bash
python main.py --file sample_data.xlsx
```

### REST API

```bash
python main.py --url https://jsonplaceholder.typicode.com/users
```

# Pipeline Workflow

```
Load Dataset
      │
      ▼
Inspect Dataset
      │
      ▼
Clean Dataset
      │
      ▼
Generate Report
      │
      ▼
Export Output
```



# Sample Datasets

The repository contains sample CSV, JSON and Excel datasets for testing.


# Current Version

**V3**

# Planned Improvements

- Data validation
- Logging system
- Configurable cleaning strategies
- Database support (MySQL/PostgreSQL)
- Multiple file processing
- Better exception handling
- YAML/JSON configuration support
- Unit tests



# Technologies Used

- Python
- Pandas
- Rich
- Requests
- Argparse
- OpenPyXL
- Sys