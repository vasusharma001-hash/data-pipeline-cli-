#this file is created to clean the missing values and duplicates value in data

import pandas as pd

def clean_duplicates(df:pd.DataFrame , strategy) -> pd.DataFrame:

    if strategy == "keep":
        return(df)
    
    elif strategy == "remove":
     return df.drop_duplicates()

def handle_missing_values(df:pd.DataFrame , strategy) -> pd.DataFrame:

    if strategy == "drop":
     return df.dropna() 
    
    elif strategy == "mean":
       return df.fillna(df.mean(numeric_only = True))
    
    elif strategy == "median":
       return df.fillna(df.median(numeric_only = True))
    
    elif strategy == "mode":
       return df.fillna(df.mode().iloc[0])
    
    elif strategy == "keep":
       return(df)


