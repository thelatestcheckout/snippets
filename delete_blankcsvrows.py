import csv

with open('indianmalenames.csv', newline='') as in_file:
    with open('indianmalenames1.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row:
                writer.writerow(row)
