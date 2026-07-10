import pandas as pd
import requests
import sys
import os

LARGE_FILE_THRESHOLD = 100 * 1024 * 1024      # 100 MB
DEFAULT_CHUNK_SIZE = 10000                    # rows


def load_data(args_file):

    file_size = os.path.getsize(args_file)

    # CSV
    if args_file.endswith(".csv"):

        if file_size > LARGE_FILE_THRESHOLD:
            print("Large dataset detected.")
           
            return pd.read_csv(
                args_file,
                chunksize=DEFAULT_CHUNK_SIZE
            )

        return pd.read_csv(args_file)

    # JSON
    elif args_file.endswith(".json"):
        return pd.read_json(args_file)

    # Excel
    elif args_file.endswith(".xlsx"):
        return pd.read_excel(args_file)

    else:
        print("File format not supported.")
        sys.exit(1)


def load_api(url):

    try:
        response = requests.get(url)
        response.raise_for_status()

        api_data = response.json()

        new_df = pd.json_normalize(api_data)
        return new_df

    except requests.exceptions.RequestException as e:
        print(f"API error : {e}")
        sys.exit(1)