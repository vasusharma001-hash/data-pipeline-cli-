import pandas as pd 
import requests
import sys



def load_data(args_file):

    if args_file.endswith(".csv"):
     return pd.read_csv(args_file) #for processing csv files
     
    elif args_file.endswith(".json"):
      return pd.read_json(args_file)  #for processing json files
     
    elif args_file.endswith(".xlsx"):
      return pd.read_excel(args_file)
    
    else :
     print("file format not supported")
     sys.exit()
     

def load_api(url):

    try:
       response = requests.get(url)
       response.raise_for_status()

       api_data = response.json()

       new_df = pd.json_normalize(api_data)
       return(new_df)

    except requests.exceptions.RequestException as e:
     print(f"API error : {e}")
    sys.exit()








 
