import sys


def export_output(cleaned_df, args_file, append=False):

    if args_file.endswith(".csv"):

        if append:
            cleaned_df.to_csv(
                args_file,
                index=False,
                mode="a",
                header=False
            )

        else:
            cleaned_df.to_csv(
                args_file,
                index=False,
                mode="w",
                header=True
            )
            print("output file : output.csv")


    elif args_file.endswith(".xlsx"):

        cleaned_df.to_excel(
            args_file,
            index=False
        )
        print("output file : output.xlsx")


    elif args_file.endswith(".json"):

        cleaned_df.to_json(
            args_file,
            orient="records",
            indent=4
        )
        print("output file : output.json")
    else:
        print("Output File Not Supported")
        sys.exit(1)


def export_api(cleaned_df, args_file):

     if args_file.endswith(".json"):

        cleaned_df.to_json(
            args_file,
            orient="records",
            indent=4
        )
        print("Output file : Output.json")


     else:
        print("Output File Not Supported")
        sys.exit(1)

