import json

input_filepath = '/Users/ashu/Desktop/snippets/input/json/val.json'

jsondata = open(input_filepath)
data = json.load(jsondata)
for item in data:
    count = 0
    for x in item['argumentative']:
        if(x == 'y'):
            count = count + 1

    if count < 2:
        data.remove(item)
        break

json_string = json.dumps(data)
print(json_string)
