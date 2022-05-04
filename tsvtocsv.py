import re

# tab separated csv file
input_filepath = 'input.csv'

# comma sepatated csv file
output_filepath = 'output.csv'


def tabtocomma(input_filepath, output_filepath):
    with open(input_filepath, 'r', encoding="ISO-8859-1") as myfile:
        with open(output_filepath, 'w') as csv_file:
            for line in myfile:
                fileContent = re.sub("\t", ",", line)
                csv_file.write(fileContent)
    print("Successfully made csv file")


tabtocomma(input_filepath, output_filepath)
