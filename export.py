def export_output(cleaned_df , args_file):
    if args_file.endswith(".csv"):
     cleaned_df.to_csv("output.csv" , index=False)

    elif args_file.endswith(".xlsx"):
      cleaned_df.to_excel("output.xlsx" , index =False)


    elif args_file.endswith(".json"):
     cleaned_df.to_json(
                    "output.json",
                    orient="records",
                    indent=4


     )
    print("output saved")