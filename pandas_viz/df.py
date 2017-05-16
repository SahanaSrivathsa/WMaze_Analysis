import pandas as pd

rawDataDir = '/Volumes/ls 1/BarnesLab/RawData'

with open('rats.csv','r') as rats:
    lines = rats.readlines()
rows = [line.split(',') for line in lines if line != lines[0]]

oldRats = [row[0] for row in rows if int(row[1]) == 25]
youngRats = [row[0] for row in rows if int(row[1]) == 10]

oldDataframes = [pd.read_csv('{0}/{1}/SessionInfo_{1}.csv'.format(rawDataDir,rat))[['Session','Session Length','Correct','Initial Error','Outbound Errors','Inbound Errors',
                 'Repeat Errors','Total Errors','Total Feeder Visits']] for rat in oldRats]
youngDataframes = [pd.read_csv('{0}/{1}/SessionInfo_{1}.csv'.format(rawDataDir,rat))[['Session','Session Length','Correct','Initial Error','Outbound Errors','Inbound Errors',
                 'Repeat Errors','Total Errors','Total Feeder Visits']] for rat in youngRats]









