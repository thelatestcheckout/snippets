import json
from sklearn.model_selection import train_test_split

input_filepath = 'input.json'


def splitJson(input_filepath):
    input = open(input_filepath)
    data = json.load(input)

    # train data = 70%, remain = 30% (test and validation data)
    train, remain = train_test_split(data, train_size=0.7)
    # remain = 100%, val = 1/3 (which means 10% of whole data), test = 2/3 (which means 20% of whole data)
    val, test = train_test_split(remain, test_size=2/3)

    with open('train.json', 'w') as fp1:
        json.dump(train, fp1, indent=2)

    with open('test.json', 'w') as fp2:
        json.dump(test, fp2, indent=2)

    with open('val.json', 'w') as fp3:
        json.dump(val, fp3, indent=2)


splitJson(input_filepath)
