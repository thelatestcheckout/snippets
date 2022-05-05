import pandas as pd

# tab separated csv file
input_filepath = 'input.csv'

# comma sepatated csv file
output_filepath = 'output.csv'

# You need to tell Pandas that the file is tab delimited when you import it.
# You can pass a delimiter to the read_csv method but in your case,
# since the delimiter changes by file, you want to pass None -
# this will make Pandas auto-detect the correct delimiter.
data = pd.read_csv(input_filepath, sep=None, engine='python')
data.to_csv(output_filepath, encoding="utf-8", index=False)
