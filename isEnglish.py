import csv

# word = "कान्‍ता"
# if word.encode().isalpha():
#     print("It is English")
# else:
#     print("It is not English")

with open('indianmalenames2.csv', newline='') as in_file:
    with open('indianmalenames3.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if row[0].encode().isalpha():
                writer.writerow(row)
