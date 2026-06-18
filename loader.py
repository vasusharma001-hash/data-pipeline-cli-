import pandas as pd 
import sys

def load_data(args_file):

    if args_file.endswith(".csv"):
     return pd.read_csv(args_file) #for processing csv files
     
    elif args_file.endswith(".json"):
      return pd.read_json(args_file)  #for processing json files
     
    elif args_file.endswith(".xlsx"):
      return pd.read_excel(args_file)
    else :
     print("file format not supoorted")
     sys.exit()
     


