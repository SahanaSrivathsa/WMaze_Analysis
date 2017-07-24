import pandas as pd
import os

ratNums = pd.read_csv('/Users/adelekap/Documents/WMaze_Analysis/pandas_viz/rats.csv')
youngRats = list(ratNums[ratNums['AGE'] == 10]['RAT'])
oldRats = list(ratNums[ratNums['AGE'] == 25]['RAT'])

youngData = pd.DataFrame()
oldData = pd.DataFrame()

dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data'
files = os.listdir(dir)
for y in youngRats:
    os.chdir(dir + '/'+ str(y))
    y_rat = pd.read_csv(str(y)+'_DATA.csv')
    youngData[str(y)] = y_rat['Correct/Incorrect']
for o in oldRats:
    os.chdir(dir+'/'+str(o))
    o_rat = pd.read_csv(str(o)+'_DATA.csv')
    oldData[str(o)] = o_rat['Correct/Incorrect']

youngDataNew = youngData.transpose()
oldDataNew = oldData.transpose()
youngDataNew.to_csv(dir+'/youngData.csv')
oldDataNew.to_csv(dir+'/oldData.csv')
