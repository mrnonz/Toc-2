import csv
import numpy as np
import matplotlib.pyplot as plt

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


x = np.array(dataX)
y = np.array(dataY)

# rewrite line equation
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y)[0]

# print (m, c)
