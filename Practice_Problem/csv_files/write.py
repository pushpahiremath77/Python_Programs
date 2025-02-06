import csv
with open('data.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name', 'Age'])  
    csv_writer.writerow(['John', 30])     
