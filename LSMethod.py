import csv
import numpy as np
import matplotlib.pyplot as plt

dataX = []
dataY = []


def multiplyList(dataList, number):
    newList = []

    for item in dataList:
        newList.append(float(item)*number)

    return newList


def addList(dataList, number):
    newList = []

    for item in dataList:
        newList.append(float(item)+number)

    return newList

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

equation = x
equation = multiplyList(equation, m)
equation = addList(equation, c)

print "Equation have m = %s and c = %s" % (m, c)
print "Formula is y = %sx + %s" % (m, c)

plt.plot(x, y, 'o', label='Raw data', markersize=3)
plt.plot(x, equation, 'r', label='Fitted line')
plt.legend()
plt.show()
