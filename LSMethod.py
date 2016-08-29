import csv

with open('LS.csv', 'rb') as fileLS:
    reader = csv.reader(fileLS)

    thisData = False
    for row in reader:
        if thisData:
            print "%s %s " % (row[0], row[1])

        thisData = True
