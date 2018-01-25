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

def transform_data(numOfSessions,anType):
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
    plot(allData,anType,numOfSessions)

def plot(data,anType,num):
    colors = ["green", "purple"]
    sns.pointplot(x='Session',y='% Correct',data=data,hue='Age',palette=sns.xkcd_palette(colors),capsize=0.1,errwidth=2)
    plt.legend(loc=4)
    plt.title(anType.upper())
    plt.savefig('/Users/adelekap/Documents/WMaze_Analysis/Paper/plots/propCorrect/'+anType+str(num)+'.pdf')
    plt.show()

if __name__ == '__main__':
    transform_data(14,'inbound')
    transform_data(14,'outbound')
    transform_data(21,'inbound')
    transform_data(21,'outbound')



