import csv
import json

# comma sepatated csv file
input_filepath = 'input.csv'

# output json file
output_filepath = 'output.json'


def make_json(csvFilePath, jsonFilePath):
    data = []
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            id = rows.get('#id')

            # check if a row already exists
            if not (any(x.get('id') == id for x in data)):
                od = outputData(id)
                data.append(od.__dict__)
            else:
                # if row already exists, find the index of id
                for index, item in enumerate(data):
                    if item.get('id') == id:
                        break
                    else:
                        index = -1

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


class outputData():
    def __init__(self, id):
        self.id = id


make_json(input_filepath, output_filepath)
