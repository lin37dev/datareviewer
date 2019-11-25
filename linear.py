import pandas as pd
from matplotlib import pyplot as plt
import glob
# from matplotlib.pyplot import savefig

# pre-load files and generating the needing variables
path = input('Please select the path contains the csv files you want to plot.')
allFiles = glob.glob(path + '/*.csv')
fileCount = len(allFiles)
counter = 0

# move file data to x and y variables to plot
for fileName in allFiles:
    data = pd.read_csv(fileName)
    locals()['x' + str(counter)] = data['Vd']
    locals()['y' + str(counter)] = data['Id']
    plt.plot(locals()['x' + str(counter)], locals()['y' + str(counter)])
    counter = + 1

# graph styles
plt.xlabel('Vd(V)')
plt.ylabel('Id(A)')
plt.title('Graph')
plt.legend('data')
plt.show()

# graph export
# savefig('Graph', dpi=300, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format='pdf',
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None, metadata=None)
