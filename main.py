import argparse 
import sys
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

if args.input.endswith(".csv"):
     df =  pd.read_csv(args.input) #for processing csv files
     print(df)
elif args.input.endswith(".json"):
  df = pd.read_json(args.input)  #for processing json files

else :
  print("file format not supoorted")
  sys.exit()

inspect_data(df)
show_report(df , "BEFORE CLEANING")


cleaned_df = clean_duplicates(df)
cleaned_df = handle_missingvalues(cleaned_df)



inspect_data(cleaned_df)
show_report(cleaned_df ,"AFTER CLEANING")


if args.input.endswith(".csv"):
 cleaned_df.to_csv("output.csv" , index=False)

elif args.input.endswith(".json"):
 cleaned_df.to_json(
                    "output.json",
                    orient="records",
                    indent=4


)
print("Output saved" )