import csv

csv_file = 'data.csv'

with open(csv_file, mode='r', newline='') as file:
    
    reader = csv.reader(file)

    for row in reader:
        print(', '.join(row))
