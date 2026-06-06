# Data Pipeline CLI Tool

A command-line tool for cleaning, inspecting, and exporting CSV and JSON datasets.

## Problem

Real-world datasets are often messy and difficult to inspect manually. Common issues include:

* Duplicate records
* Missing values
* Inconsistent data quality

This project automates basic data inspection and cleaning tasks, allowing users to quickly prepare CSV and JSON datasets for further analysis.

## Features

* Load CSV AND JSON files
* Inspect dataset information
* Remove duplicate rows
* Remove rows containing missing values
* Generate dataset summaries
* Save cleaned data to a new CSV OR JSON file as per requirements 


## Project Structure

```text
data-pipeline-cli/
main.py
cleaner.py
inspector.py
display.py 
sample_data.csv 
sample_data.json
requirements.txt
README.md 
.gitignore
```

### Files

* `main.py` – Entry point and workflow controller
* `cleaner.py` – Data cleaning functions
* `inspector.py` – Dataset inspection and summary functions
* `display.py` -  Rich terminal report generation
## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt

```

## Usage

Run the tool using  CSV and JSON file as input:

```bash
python main.py --input sample_data.csv
```
```bash
python main.py --input sample_data.json
```
The tool will:

1. Load the dataset
2. Inspect the data
3. Remove duplicate rows
4. remove rows with missing values
5. Generate a summary
6. Save the cleaned dataset

## Sample Dataset

A small sample CSV and JSON file is included to demonstrate the tool's functionality and expected input format.

## Current Version

V2

## Future Improvements
* Excel support
* Logging
* Enhanced error handling
* Configurable cleaning options

## Technologies Used

* Python
* Pandas
* Argparse
* rich
```
```
