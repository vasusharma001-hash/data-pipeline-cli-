#this file is created for inspecting data

import pandas as pd

def inspect_data(df:pd.DataFrame) -> None:
    
    print("\n ...DATASET INFO...")
    (df.info())

   
    print("\n... NO OF COLUMNS")
    print(df.columns)

    print("\n...SHAPE..")
    print(df.shape)

    print("\n...MISSING VALUES...")
    print(df.isnull().sum())

    print("\n...DUPLICATES...")
    print(df.duplicated().sum())

    print("\n...STATISTICS...")
    print(df.describe())

