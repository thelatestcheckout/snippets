import pandas as pd
file_name = "indianmalenames1.csv"
file_name_output = "indianmalenames2.csv"

df = pd.read_csv(file_name)
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(file_name_output, index=False)
