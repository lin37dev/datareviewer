# It is now possible to sort and plot a path of files, whoes names were not delicately designed.

import pandas as pd
from matplotlib import pyplot as plt
import glob

# pre-load files
plt.style.use('mystyle.mplstyle')
plotPath = input('Please select the path contains the csv files you want to plot.')
# plt.style.use(input('Please select theme'))
allFiles = glob.glob(plotPath + '/*.csv')
i = 0


# get headers and indices.
def getHeaders():
    temp1 = allFiles[0]
    data1 = pd.read_csv(temp1)
    headings = data1.columns.values
    return headings


headers = getHeaders()
plt.figure(figsize=(11, 8))
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.yscale('log')


def getIndex():
    tempIndex = []
    for tempFile in allFiles:
        tempData = pd.read_csv(tempFile)
        if max(tempData[headers[0]]) > 0:
            tempIndex.append(max(tempData[headers[0]]))
        else:
            tempIndex.append(min(tempData[headers[0]]))
    return tempIndex


while len(allFiles):
    for fileName in allFiles:
        index = getIndex()
        data = pd.read_csv(fileName)
        locals()['x' + str(i)] = data[headers[0]]
        if max(data[headers[0]]) > 0:
            if max(data[headers[0]]) == max(index):
                locals()['y' + str(i)] = data[headers[1]]
                plt.plot(locals()['x' + str(i)], locals()['y' + str(i)])
                index.remove(max(index))
                allFiles.remove(fileName)
        else:
            if min(data[headers[0]]) == min(index):
                locals()['y' + str(i)] = abs(data[headers[1]])
                plt.plot(locals()['x' + str(i)], locals()['y' + str(i)])
                index.remove(min(index))
                allFiles.remove(fileName)
        i = + 1
plt.show()
exit()
