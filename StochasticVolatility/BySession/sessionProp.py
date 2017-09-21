import pandas as pd
import matplotlib.pyplot as plt

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
    for row in range(0,len(ydata)):
        x = range(1, 15)
        yy = ydata.iloc[row]
        plt.plot(x,yy,color='g',alpha = 0.3)
    plt.plot(x,list(ydata.mean()),color='g',lw=2)
    for row in range(0,len(odata)):
        x = range(1, 15)
        oy = odata.iloc[row]
        plt.plot(x,oy,color='purple',alpha = 0.3)
    plt.plot(x,list(odata.mean()),color='purple',lw=2)

    plt.xlim([1,14])
    plt.savefig(anType+'Proportion.pdf')
    plt.show()


if __name__ == '__main__':
    plot('inbound')
    plot('outbound')
