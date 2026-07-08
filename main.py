import argparse 
from rich import print
from cleaner import clean_duplicates , handle_missing_values
from loader import load_api , load_data
from export import export_api , export_output
from display import show_report , show_columns , show_shape



parser = argparse.ArgumentParser()
parser.add_argument("--file" ,
                    help = "INPUT CSV , JSON AND EXCEL FILES"
                    )

parser.add_argument("--url",
                     type = str ,
                     help = "REST API URL" # tells the user what to give as input in --url
                                              
                     )
parser.add_argument("--duplicates",
                    type = str,
                    choices=["remove" , "keep"],
                    default="remove",
                    help= "Duplicate Handling Strategy"
                     )

parser.add_argument("--missing",
                    type= str ,
                    choices= ["drop" , "keep" ,
                              "mean", "mode", "median"],
                    default= "drop",
                    help= "Missing Values Handling Strategy"

                    )

args = parser.parse_args()


if args.file:
 df = load_data(args.file)


elif args.url:
 df = load_api(args.url)


show_shape(df.shape , "DATABASE SHAPE")
show_columns(df.columns , "INDEX")
show_report(df , "BEFORE CLEANING")


cleaned_df = clean_duplicates(df , args.duplicates)
cleaned_df = handle_missing_values(cleaned_df , args.missing)


#inspect_data(cleaned_df) 
show_report(cleaned_df ,"AFTER CLEANING")


if args.file:
  export_output(cleaned_df , args.file)

elif args.url:
 export_api(cleaned_df)

