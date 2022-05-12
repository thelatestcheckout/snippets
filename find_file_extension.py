import sys
import os


input_filepath = sys.argv[1]
filepath, file_extension = os.path.splitext(input_filepath)
print(filepath)
print(file_extension)

# run it with the following command
# python3 findfileextension.py /Users/ashu/Desktop/snippets/input/csv/input.csv
