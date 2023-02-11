import csv

output = open('output_test.csv', 'w')

line = ['Красный', 'Синий']
writer = csv.writer(output)
writer.writerow(line)
writer.writerow(line)
writer.writerow(line)

output.close()