import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dataDir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'

rats = pd.read_csv('/Users/adelekap/Documents/WMaze_Analysis/pandas_viz/rats.csv')
youngRats = list(rats[rats['AGE']==10]['RAT'])
oldRats = list(rats[rats['AGE']==25]['RAT'])

def getData(rats):
    df = pd.DataFrame()
    for rat in rats:
        temp = pd.read_csv('{0}{1}/{1}_DATA.csv'.format(dataDir,rat))
        tempout = temp[temp['Feeder #']!= 2]
        out = tempout[tempout['Trial Type'] == 'Out']
        out['RAT'] = rat
        df = df.append(out[out['Correct/Incorrect']==0])
    return df


youngRatData = getData(youngRats)
oldRatData = getData(oldRats)

concatYoung = youngRatData
concatYoung['AGE'] = 'Young'
concatOld = oldRatData
concatOld['AGE'] = 'Old'
combinedData = pd.concat([concatYoung,concatOld])

fig, ax =plt.subplots(1,2)
sns.countplot(y="Feeder #", data=youngRatData, palette="Greens_d",ax=ax[0])
sns.countplot(y='Feeder #', data=oldRatData, palette ='Purples_d',ax=ax[1])
plt.show()



