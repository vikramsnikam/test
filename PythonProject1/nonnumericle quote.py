import csv
with open('plot.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('plot.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])



