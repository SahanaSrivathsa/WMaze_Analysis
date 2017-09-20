import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def getData(anType,group):
    dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'
    data_denom = pd.read_csv(dir + anType + group + 'Denom.csv').iloc[:,1:]# csv of total trials for each day
    data_numAll = pd.read_csv(dir + anType + group + 'Num.csv').iloc[:,1:]# correct per day
    out = pd.DataFrame()
    meanprop = (data_numAll/data_denom).mean()
    out[anType+' proportion'] = meanprop
    out['age'] = group
    out[anType+' total'] = data_denom.mean()
    out['Session'] = range(1,len(out['age'])+1)
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




inYoungProp = getData('inbound','Young')
inOldProp = getData('inbound','Old')

inbound = pd.concat([inYoungProp,inOldProp])

sns.jointplot()

outYoungProp = getData('outbound','Young')
outOldProp = getData('outbound','Old')

test = inYoungProp.mean()

print 'test'

#sns.jointplot(pd.Series(range(1,15)),0,inYoung)
#inYoung['Session'] = range(1,15)

#sns.jointplot()


