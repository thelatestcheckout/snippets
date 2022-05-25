from csv import writer

name = input("Enter the name: ")
gender = input("Enter gender(m/f): ")
list_data = [name, gender, "indian"]
# list_data.append(name)
# list_data.append(gender)
# list_data.append("indian")

# list_data = ['shyani', 'f', 'indian']
with open('input/csv/short.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(list_data)
    f_object.close()
