import argparse
import os
import pandas as pd

from cleaner import clean_duplicates, handle_missing_values
from loader import load_api, load_data
from export import export_api, export_output
from display import (
    show_report,
    show_columns,
    show_shape,
    show_large_dataset_info
)


parser = argparse.ArgumentParser()

parser.add_argument(
    "--file",
    help="INPUT CSV , JSON AND EXCEL FILES"
)

parser.add_argument(
    "--url",
    type=str,
    help="REST API URL"
)

parser.add_argument(
    "--duplicates",
    type=str,
    choices=["remove", "keep"],
    default="remove",
    help="Duplicate Handling Strategy"
)

parser.add_argument(
    "--missing",
    type=str,
    choices=["drop", "keep", "mean", "mode", "median"],
    default="drop",
    help="Missing Values Handling Strategy"
)

args = parser.parse_args()

# Decide output file based on input file

output_file = None

if args.file:

    if args.file.endswith(".csv"):
        output_file = "output.csv"

    elif args.file.endswith(".json"):
        output_file = "output.json"

    elif args.file.endswith(".xlsx"):
        output_file = "output.xlsx"

elif args.url:
    output_file = "output.json"


# ===================== FILE INPUT ===================== #

if args.file:

    data = load_data(args.file)

    # ---------- NORMAL LOADING ---------- #

    if isinstance(data, pd.DataFrame):

        show_shape(data.shape, "DATASET SHAPE")
        show_columns(data.columns)
        show_report(data, "BEFORE CLEANING")

        cleaned_data = clean_duplicates(data, args.duplicates)
        cleaned_data = handle_missing_values(cleaned_data, args.missing)

        show_report(cleaned_data, "AFTER CLEANING")

        export_output(
        cleaned_data,
        output_file,
        append=False
        
        )
        

        

    # ---------- CHUNK LOADING ---------- #

    else:

        file_size = os.path.getsize(args.file) / (1024 * 1024)

        show_large_dataset_info(
         args.file,
         file_size
        )

        print("Processing dataset...\n")
 
        first_chunk = True 
        total_rows = 0

        for chunk in data:

            total_rows += len(chunk)

            chunk = clean_duplicates(chunk, args.duplicates)
            chunk = handle_missing_values(chunk, args.missing)

            export_output(
             chunk,
              output_file,
              append=not first_chunk
              )

            first_chunk = False

        print("\nProcessing completed.")
        print(f"Rows Processed : {total_rows:,}")
        print(f"Output File    : {output_file}") 
    print("Output Saved.")


# ===================== API INPUT ===================== #

elif args.url:

    df = load_api(args.url)

    show_shape(df.shape, "DATASET SHAPE")
    show_columns(df.columns)
    show_report(df, "BEFORE CLEANING")

    cleaned_df = clean_duplicates(df, args.duplicates)
    cleaned_df = handle_missing_values(cleaned_df, args.missing)

    show_report(cleaned_df, "AFTER CLEANING")

    export_api(
    cleaned_df,
    output_file
)
    print("Output Saved.")

else:
    parser.print_help()