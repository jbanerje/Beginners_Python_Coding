#Python - File read write operation

import csv
with open('test.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
                print(', '.join(row))
