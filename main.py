import argparse 
import pandas as pd
from inspector import inspect_data
from cleaner import clean_duplicates
from cleaner import handle_missingvalues

parser = argparse.ArgumentParser()
parser.add_argument("--input")
args = parser.parse_args()
print(args.input)

df =  pd.read_csv(args.input)

print("\n...ORIGINAL DATA...")
print(df)
print("\n ...BEFORE CLEANING...")
inspect_data(df)

cleaned_df = clean_duplicates(df)
cleaned_df = handle_missingvalues(df)
print("\n...FINAL DATA...")
inspect_data(cleaned_df)


cleaned_df.to_csv("output.csv" , index=False)

