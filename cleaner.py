#this file is created to clean the missing values and duplicates value in data

import pandas as pd

def clean_duplicates(df:pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

def handle_missingvalues(df):
    return df.dropna()


