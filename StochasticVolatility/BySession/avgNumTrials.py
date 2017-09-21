import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats as st


"""
This creates two plots:
(1) A plot of the average number of inbound trials for young and old
(2) A plot of the average number of outbound trials for young and old
"""

def getData(anType,group):
    dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'
    data_total = pd.read_csv(dir + anType + group + 'Denom.csv').iloc[:,1:]# csv of total trials for each day
    data_total['age'] = group
    return data_total

def plot(x, y, yerr1,yerr2, data,type):
    plt.figure()
    plt.style.use('ggplot')
    plt.ylabel("Number of Trials")
    ax = plt.gca()
    ax2 = ax.twinx()
    young = data[data['Age']=='Young']
    old = data[data['Age'] == 'Old']
    young.plot(x=x, y=y, yerr=yerr1, kind="bar", ax=ax,color="green",position=0,width=0.25,
               error_kw=dict(ecolor='black', lw=1, capsize=2, capthick=1),legend=False)
    old.plot(x=x,y=y,yerr=yerr2,kind="bar",ax=ax2,color="purple",position=1,width=0.25,
             error_kw=dict(ecolor='black', lw=1, capsize=2, capthick=1),legend=False)
    ax2.grid(False)
    ax2.get_yaxis().set_visible(False)
    plt.savefig(type+'MeanNumTrials.pdf')
    plt.show()

def create(type):
    YoungTotal = getData(type,'Young')
    OldTotal = getData(type,'Old')
    df = pd.concat([YoungTotal,OldTotal])

    grouped = df.groupby(['age'])
    means = grouped.mean()
    ci = grouped.aggregate(lambda x: st.sem(x) * 1.645) #90% confidence interval

    plotData = pd.DataFrame()
    plotData['Session'] = range(1,15)+range(1,15)
    plotData['Age'] = ['Young' for i in range(1,15)]+['Old' for i in range(1,15)]
    plotData['Mean'] = list(means.loc['Young']) + list(means.loc['Old'])
    plotData['youngCI'] = list(ci.loc['Young']) + list(ci.loc['Young'])
    plotData['oldCI'] = list(ci.loc['Old']) + list(ci.loc['Old'])
    plot("Session", "Mean", "youngCI","oldCI",plotData,type)


if __name__ == "__main__":
    create('inbound')
    create('outbound')