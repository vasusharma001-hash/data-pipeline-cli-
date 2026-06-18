# Data Pipeline CLI Tool

A command-line tool for loading, cleaning, inspecting, and exporting structured datasets.

## Problem

Real-world datasets are often messy and difficult to inspect manually. Common issues include:

* Duplicate records
* Missing values
* Poor data quality

This project automates basic data inspection and cleaning tasks, allowing users to quickly prepare datasets for further analysis.


## Features

* Load CSV, JSON, and Excel (.xlsx) files
* Inspect dataset information
* Remove duplicate rows
* Remove rows containing missing values
* Generate dataset summaries
* Display reports in a formatted terminal UI using Rich
* Export cleaned datasets back to CSV, JSON, or Excel format


## Supported File Formats

### Input

* CSV (.csv)
* JSON (.json)
* Excel (.xlsx)

### Output

* CSV (.csv)
* JSON (.json)
* Excel (.xlsx)


## Project Structure

```text
data-pipeline-cli/

main.py
loader.py
cleaner.py
inspector.py
display.py
export.py

sample_data.csv
sample_data.json
sample_data.xlsx

requirements.txt
README.md
.gitignore
```

## Files

* `main.py` - Entry point and workflow controller
* `loader.py` - File loading functions
* `cleaner.py` - Data cleaning functions
* `inspector.py` - Dataset inspection functions
* `display.py` - Rich terminal report generation
* `export.py` - Export cleaned datasets


## Installation

Clone the repository and install dependencies.

```bash
git clone https://github.com/vasusharma001-hash/data-pipeline-cli-.git

cd data-pipeline-cli

pip install -r requirements.txt
```


## Usage

Run the tool with any supported file type.

```bash
python main.py --file sample_data.csv
```

```bash
python main.py --file sample_data.json
```

```bash
python main.py --file sample_data.xlsx
```

The tool will:

1. Load the dataset
2. Inspect the data
3. Remove duplicate rows
4. Remove rows with missing values
5. Generate a summary report
6. Export the cleaned dataset


## Sample Datasets

The repository includes sample CSV, JSON, and Excel datasets to demonstrate the expected input format.


## Current Version

V2


## Future Improvements

* Multiple file processing support
* Logging system
* Enhanced error handling
* Configurable cleaning strategies
* Database support (MySQL/PostgreSQL)
* API data ingestion
* User Interface (UI)


## Technologies Used

* Python
* Pandas
* Rich
* Argparse
* OpenPyXL
* Sys
