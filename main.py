import argparse 
from rich import print
import pandas as pd
from cleaner import clean_duplicates , handle_missingvalues
from loader import load_api , load_data
from export import export_api , export_output
from display import show_report , show_columns , show_shape



parser = argparse.ArgumentParser()
parser.add_argument("--file" ,
                    help = "INPUT CSV , JSON AND EXCEL FILES")
parser.add_argument("--url",
                     type = str ,
                     help = "REST API URL" # tells the user what to give as input in --url
                                              
                     )

args = parser.parse_args()


if args.file:
 df = load_data(args.file)


elif args.url:
 df = load_api(args.url)


show_shape(df.shape , "DATABASE SHAPE")
show_columns(df.columns , "INDEX")
show_report(df , "BEFORE CLEANING")


cleaned_df = clean_duplicates(df)
cleaned_df = handle_missingvalues(cleaned_df)


#inspect_data(cleaned_df) 
show_report(cleaned_df ,"AFTER CLEANING")


if args.file:
  export_output(cleaned_df , args.file)

elif args.url:
 export_api(cleaned_df)

