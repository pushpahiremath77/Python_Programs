import csv

with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)


import csv
with open('data.csv','r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

