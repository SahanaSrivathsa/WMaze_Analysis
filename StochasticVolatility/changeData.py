
import pandas as pd
import os

data = pd.DataFrame()

dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data'
files = os.listdir(dir)
for file in files:
    os.chdir(dir + '/'+ file)
    rat = pd.read_csv(file+'_DATA.csv')
    data[file] = rat['Correct/Incorrect']

dataNew = data.transpose()
dataNew.to_csv('datanew.csv')


