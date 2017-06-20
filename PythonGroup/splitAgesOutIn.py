import pandas as pd
import os

ratNums = pd.read_csv('/Users/adelekap/Documents/WMaze_Analysis/pandas_viz/rats.csv')
youngRats = list(ratNums[ratNums['AGE'] == 10]['RAT'])
oldRats = list(ratNums[ratNums['AGE'] == 25]['RAT'])


youngDataOut = pd.DataFrame()
youngDataIn = pd.DataFrame()
oldDataOut = pd.DataFrame()
oldDataIn = pd.DataFrame()

dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data'
files = os.listdir(dir)
for y in youngRats:
    os.chdir(dir + '/'+ str(y))
    y_rat = pd.read_csv(str(y)+'_DATA.csv')
    youngDataOut[str(y)] = y_rat[y_rat['Trial Type'] == 'Out']['Correct/Incorrect']
    youngDataIn[str(y)] = y_rat[y_rat['Trial Type'] == 'In']['Correct/Incorrect']
for o in oldRats:
    os.chdir(dir+'/'+str(o))
    o_rat = pd.read_csv(str(o)+'_DATA.csv')
    oldDataOut[str(o)] = o_rat[o_rat['Trial Type'] == 'Out']['Correct/Incorrect']
    oldDataIn[str(o)] = o_rat[o_rat['Trial Type'] == 'In']['Correct/Incorrect']

youngNewOut = youngDataOut.transpose()
# youngNewIn = youngDataIn.transpose()
# oldNewOut = oldDataOut.transpose()
# oldNewIn = oldDataIn.transpose()

youngNewOut.to_csv(dir+'/youngOut.csv')
# youngNewIn.to_csv(dir+'/youngIn.csv')
# oldNewOut.to_csv(dir+'/oldOut.csv')
# oldNewIn.to_csv(dir+'/oldIn.csv')
