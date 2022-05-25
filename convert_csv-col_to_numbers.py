from asyncore import read
from cmath import log
import csv


def convertNamesToNumbers(input):
    input = input.lower()
    output = []
    for character in input:
        number = ord(character) - 96
        output.append(number)
    for i in range(50):
        if len(output) < 50:
            output.append(0)

    return output


def logic(input_file, output_file):
    with open(input_file, newline='') as in_file:
        with open(output_file, 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            reader = csv.reader(in_file)
            next(reader, None)
            for row in reader:
                row[0] = convertNamesToNumbers(row[0])
                if(row[1] == 'm'):
                    row[1] = 1
                else:
                    row[1] = 0
                writer.writerow((row[0], row[1]))


if __name__ == "__main__":
    input_file = "combined.csv"
    output_file = "combined_numeric.csv"
    logic(input_file, output_file)
