import pandas as pd

# tab separated csv file
input_filepath = 'input/tsv/small.csv'

# comma sepatated csv file
output_filepath = 'output/output.csv'

# tsv_to_csv.py
data = pd.read_csv(input_filepath, sep=None, engine='python')
print(type(data))
df = pd.DataFrame(data)
df = df.reset_index()  # make sure indexes pair with number of rows
for index, row in df.iterrows():
    print(row['stance'])
