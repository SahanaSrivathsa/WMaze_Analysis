import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

""""
Creates a plot of the proportion correct for each rat and the mean
Saves to figs: inbound and outbound.
"""

def getData(anType,group):
    dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'
    data_num = pd.read_csv(dir + anType + group + 'Num.csv').iloc[:, 1:]
    data_total = pd.read_csv(dir + anType + group + 'Denom.csv').iloc[:, 1:]
    return (data_num/data_total)

def plot(anType):
    ydata = getData(anType,'Young')
    odata = getData(anType,'Old')
    plt.figure()
    plt.style.use('ggplot')
    omean = list(ydata.mean())[0:3]
    for k in list(odata.mean())[3:]:
        omean.append(k)
    ymean = list(odata.mean())[0:3]
    for l in list(ydata.mean())[3:]:
        ymean.append(l)
    for row in range(0,len(ydata)):
        x = range(1, 22)
        yy = ydata.iloc[row]
        plt.plot(x,yy,color='g',alpha = 0.3)
    plt.plot(x,ymean,color='g',lw=2)
    for row in range(0,len(odata)):
        x = range(1, 22)
        oy = odata.iloc[row]
        plt.plot(x,oy,color='purple',alpha = 0.3)
    plt.plot(x,omean,color='purple',lw=2)
    plt.xlabel('Session')
    plt.ylabel('Proportion Correct')
    plt.xlim([1,21])
    plt.ylim([0,1])
    green_patch = mpatches.Patch(color='green', label='Young')
    purple_patch = mpatches.Patch(color='purple', label='Old')
    plt.legend(handles=[green_patch,purple_patch],loc=4)
    plt.savefig(anType + 'Proportion.pdf')
    plt.show()


if __name__ == '__main__':
    plot('inbound')
    plot('outbound')
