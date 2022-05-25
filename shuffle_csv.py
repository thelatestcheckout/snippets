import pandas as pd
from requests import head

df = pd.read_csv('merge_csv.csv')
ds = df.sample(frac=1)
ds.to_csv('shuffle_csv.csv', index=False)
