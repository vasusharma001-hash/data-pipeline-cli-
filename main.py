import argparse 
from rich import print
import pandas as pd
from inspector import inspect_data
from cleaner import clean_duplicates
from cleaner import handle_missingvalues
from display import show_report
from loader import load_data
from export import export_output


parser = argparse.ArgumentParser()
parser.add_argument("--file")
args = parser.parse_args()
print(args.file)

df = load_data(args.file)
print(df)

inspect_data(df)
show_report(df , "BEFORE CLEANING")


cleaned_df = clean_duplicates(df)
cleaned_df = handle_missingvalues(cleaned_df)


#inspect_data(cleaned_df) 
show_report(cleaned_df ,"AFTER CLEANING")

export_output(cleaned_df , args.file)