import argparse 
from rich import print
import pandas as pd
from inspector import inspect_data
from cleaner import clean_duplicates
from cleaner import handle_missingvalues
from display import show_report




parser = argparse.ArgumentParser()
parser.add_argument("--input")
args = parser.parse_args()
print(args.input)

df =  pd.read_csv(args.input)
print(df)

inspect_data(df)
show_report(df , "BEFORE CLEANING")


cleaned_df = clean_duplicates(df)
cleaned_df = handle_missingvalues(cleaned_df)

print("CLEANED DUP COUNT:", cleaned_df.duplicated().sum())

inspect_data(cleaned_df)
show_report(cleaned_df ,"AFTER CLEANING")

cleaned_df.to_csv("output.csv" , index=False)

