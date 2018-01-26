import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""
Gets proportion CSVs and plots the mean proportion correct with standard error.
"""

def getData(anType,group,sessionNum):
    dir = '/Users/adelekap/Documents/WMaze_Analysis/Paper/data/'
    data_num = pd.read_csv('{0}{1}Session/{2}{3}Num.csv'.format(dir,str(sessionNum),anType,group)).iloc[:, 1:]
    data_total = pd.read_csv('{0}{1}Session/{2}{3}Denom.csv'.format(dir,str(sessionNum),anType,group)).iloc[:, 1:]
    return (data_num/data_total)

def errorBars(data):
    STDVs = []
    for session in range(len(data[0])): #CHANGE IF NOT JUST DOING 14 SESSIONS!
        sessionData = [data[rat][session] for rat in range(len(data))]
        STDVs.append(round(np.std(sessionData),2))
    return STDVs

def transform_data(nnumOfSessions, nanType):
    totality = []
    for numOfSessions,anType in zip(nnumOfSessions,nanType):
        ydata = getData(anType,'Young',numOfSessions)
        odata = getData(anType,'Old',numOfSessions)
        youngNum = len(ydata)
        oldNum = len(odata)

        allData = pd.DataFrame()

        propCorrect = []
        for yanimal in range(youngNum):
            propCorrect = propCorrect + list(ydata.ix[yanimal])
        for oanimal in range(oldNum):
            propCorrect = propCorrect + list(odata.ix[oanimal])

        allData['% Correct'] = propCorrect
        allData['Age'] = ['young' for i in range(youngNum*numOfSessions)]+['old' for j in range(oldNum*numOfSessions)]
        sessions = []
        for rat in range(youngNum+oldNum):
            for i in range(1,numOfSessions+1):
                sessions.append(i)
        allData['Session'] = sessions
        totality.append(allData)
    plot(totality)

def plot(allDATA):
    colors = ["green", "purple"]
    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    sns.set(font_scale=1)
    sns.pointplot(x='Session',y='% Correct',data=allDATA[0],hue='Age',palette=sns.xkcd_palette(colors),
                  capsize=0.1,errwidth=1.5,ax=ax1,scale=0.6)
    sns.pointplot(x='Session', y='% Correct', data=allDATA[1], hue='Age', palette=sns.xkcd_palette(colors),
                  capsize=0.1, errwidth=1.5, ax=ax2,scale=0.6)
    sns.pointplot(x='Session', y='% Correct', data=allDATA[2], hue='Age', palette=sns.xkcd_palette(colors),
                  capsize=0.1, errwidth=1.5, ax=ax3,scale=0.6)
    sns.pointplot(x='Session', y='% Correct', data=allDATA[3], hue='Age', palette=sns.xkcd_palette(colors),
                  capsize=0.1, errwidth=1.5, ax=ax4,scale=0.6)
    ax1.legend_.remove()
    ax2.legend_.remove()
    ax3.legend_.remove()
    ax1.set_ylim(0,1.1)
    ax2.set_ylim(0,1.1)
    ax3.set_ylim(0,1.1)
    ax4.set_ylim(0,1.1)
    ax1.set_xticklabels(['',2,'',4,'',6,'',8,'',10,'',12,'',14])
    ax2.set_xticklabels(['',2,'',4,'',6,'',8,'',10,'',12,'',14])
    ax3.set_xticklabels(['',2,'',4,'',6,'',8,'',10,'',12,'',14,'',16,'',18,'',20,''])
    ax4.set_xticklabels(['',2,'',4,'',6,'',8,'',10,'',12,'',14,'',16,'',18,'',20,''])
    plt.tight_layout()
    plt.savefig('/Users/adelekap/Documents/WMaze_Analysis/Paper/plots/propCorrect/propCorrect.pdf')
    plt.show()


if __name__ == '__main__':
    transform_data([14,14,21,21],['inbound','outbound','inbound','outbound'])


