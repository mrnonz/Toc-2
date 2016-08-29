import csv

dataX = []
dataY = []

with open('LS.csv', 'rb') as fileLS:
    reader = csv.reader(fileLS)

    thisData = False
    for row in reader:
        if thisData:
            dataX.append(row[0])
            dataY.append(row[1])
            # print "%s %s " % (row[0], row[1])

        thisData = True
