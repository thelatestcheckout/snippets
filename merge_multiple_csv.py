import pandas as pd
import glob
import os
import csv

# setting the path for joining multiple files
files = os.path.join("input/csv/", "indian*.csv")

# list of merged files returned
files = glob.glob(files)

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files))
df.to_csv('merge_csv.csv', index=False)
