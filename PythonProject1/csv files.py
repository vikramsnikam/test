import csv
with open('tab.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    print(type(reader))
    for row in reader:
        print(row)

#changed content of file

# with open('table.csv','w',newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['A','B','C'])
#     writer.writerow([1,2,3])

print('csv delimitor')

with open('table.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open('table.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        print(row)
#here '\t' can be replaced with any single word string


print('tt')
with open('tt.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)


with open('tt.csv','r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row)

print ('a')
with open('tt.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row)
#here '\t' can be replaced with any single word string result will be shown in csv file not in output


print('quote')
with open('tqt.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

print('gives double quote to numeric value')
with open('tqt.csv','r') as csvfile:
    reader = csv.reader(csvfile,quoting=csv.QUOTE_NONE)
    for row in reader:
         print(row)







