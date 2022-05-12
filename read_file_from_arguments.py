import sys

# read file from arguments
with open(sys.argv[1], 'r') as my_file:
    print(my_file.read())

# run it with the following command
# python3 readfilefromarguments.py /Users/ashu/Desktop/snippets/input/csv/input.csv
