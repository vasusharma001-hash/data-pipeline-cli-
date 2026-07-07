import pandas as pd

data = {
    "name": ["Vasu", "John", "Alice", "Vasu"],
    "age": [18, 20, 22, 18],
    "salary": [50000, 60000, None, 50000]
}
 
df = pd.DataFrame(data)

df.to_excel("sample_data.xlsx", index=False)

print("Excel file created")