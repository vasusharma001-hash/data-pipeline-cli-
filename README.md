# Data Pipeline CLI Tool

A command-line tool for cleaning, inspecting, and exporting CSV datasets.

## Problem

Real-world datasets are often messy and difficult to inspect manually. Common issues include:

* Duplicate records
* Missing values
* Inconsistent data quality

This project automates basic data inspection and cleaning tasks, allowing users to quickly prepare CSV datasets for further analysis.

## Features

* Load CSV files
* Inspect dataset information
* Remove duplicate rows
* Handle missing values
* Generate dataset summaries
* Save cleaned data to a new CSV file

## Project Structure

```text
data-pipeline-cli/
  main.py
  cleaner.py
  inspector.py
  sample_data.csv
  requirements.txt
  .gitignorREADME.md
```

### Files

* `main.py` – Entry point and workflow controller
* `cleaner.py` – Data cleaning functions
* `inspector.py` – Dataset inspection and summary functions

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the tool using a CSV file as input:

```bash
python main.py --input sample_data.csv
```

The tool will:

1. Load the dataset
2. Inspect the data
3. Remove duplicate rows
4. Handle missing values
5. Generate a summary
6. Save the cleaned dataset

## Sample Dataset

A small sample CSV file is included to demonstrate the tool's functionality and expected input format.

## Current Version

V1

## Future Improvements

* JSON support
* Excel support

* Logging
* Enhanced error handling
* Configurable cleaning options

## Technologies Used

* Python
* Pandas
* Argparse

```
```
