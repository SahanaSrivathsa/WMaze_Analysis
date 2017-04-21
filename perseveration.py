
"""
Takes Timestamps CSVs and makes heatmap with
time axis to view perseveration.
"""

import numpy as np

workingDir = "/Users/adelekap/Documents/BarnesLab/RawData/"

youngRats = [10279,10280,10348,10349]
oldRats = [10281,10282,10351,10353,10354]

def avg(list):
    sum = 0
    for num in list:
        sum += num
    if len(list) == 0:
        return 0
    return sum/len(list)



def timeseries(rat):
    #CHANGE SESSION RANGE IF MORE THAN 450 DECISIONS!!!
    files = [('{0}{1}/TimeStamps/TimeStamps_{1}_Session{2}.csv'.format(workingDir,str(rat),session)) for session in range(1,15)]
    decisions=[]
    for f in files:
        with open(f,'r') as ts:
            lines = ts.readlines()
        data = [line.split(',') for line in lines]
        for row in data:
            if row[1] == 'Correct':
                decisions.append(0)
            if row[1] == 'Repeat Error':
                decisions.append(0.3)
            if row[1] == 'Inbound Error':
                decisions.append(0.6)
            if row[1] == 'Outbound Error':
                decisions.append(1)
    return decisions[:450]

