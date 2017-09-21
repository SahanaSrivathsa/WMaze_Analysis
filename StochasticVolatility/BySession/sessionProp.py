import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats as st
import seaborn as sns
import numpy as np

def getData(anType,group):

    dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'
    data_total = pd.read_csv(dir + anType + group + 'Denom.csv').iloc[:,1:]# csv of total trials for each day
    out = data_total
    out['age'] = group
    return out

def createListData(dataframe):
    data = []
    for i in range(len(dataframe)):
        data.append(list(dataframe.iloc[0]))
    return data

def plot(anType,group,data):
    #data = list of each rat's list of proportions

    for y in data:
        x = range(1,len(y)+1)
        plt.plot(x,y)
    plt.show()



inYoungTotal = getData('inbound','Young')
inOldTotal = getData('inbound','Old')
inbound = pd.concat([inYoungTotal,inOldTotal])

data2 = inbound.groupby(['age']).mean()
data = inbound.groupby(['age']).describe()




grouped = inbound.groupby(['age'])
means = grouped.mean()
ci = grouped.aggregate(lambda x: st.sem(x) * 1.96) #95% confidence interval

plotData = pd.DataFrame()
plotData['Session'] = range(1,15)+range(1,15)
plotData['Age'] = ['Young' for i in range(1,15)]+['Old' for i in range(1,15)]
plotData['Mean'] = list(means.loc['Young']) + list(means.loc['Old'])
plotData['CI'] = list(ci.loc['Young']) + list(ci.loc['Old'])

#sns.barplot(x='Session',y='Mean',data=plotData,hue='Age')
#plt.show()

tups = [x for y in zip([(i,"Young") for i in range(1,15)],[(i,"Old") for i in range(1,15)]) for x in y]
index = pd.MultiIndex.from_tuples(tups, names=['session', 'age'])


def errplot(x, y, yerr, data):
    print plt.style.available
    plt.figure()
    plt.style.use('ggplot')
    ax = plt.gca()
    ax2 = ax.twinx()
    young = data[data['Age']=='Young']
    old = data[data['Age'] == 'Old']
    young.plot(x=x, y=y, yerr=yerr, kind="bar", ax=ax,color="green",position=0,width=0.4)
    old.plot(x=x,y=y,yerr=yerr,kind="bar",ax=ax2,color="purple",position=1,width=0.4)
    # Turns off grid on the left Axis.
    ax2.grid(False)
    # Turns off grid on the secondary (right) Axis.
    plt.show()


errplot("Session", "Mean", "CI",plotData)
print 'test'












