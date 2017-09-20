import os
import pandas as pd

"""Processes the raw data to be used in further analyses"""

df = pd.read_csv('/Users/adelekap/Documents/WMaze_Analysis/pandas_viz/rats.csv')  # Path to rats.csv
baseDir = "/Volumes/TRANS 1/BarnesLab/RawData/"  # Path to raw data file folders

rats = list(df['RAT'])


def get_data(rat):
    dataDir = baseDir + rat + "/TimeStamps/"
    files = ['TimeStamps_{1}_Session{2}.csv'.format(baseDir,rat,session) for session in range(1,15)]
    newDir = baseDir + "Processed Data/" + rat +"/"
    session = 1
    trial = 1
    type = 0  #inbound = 0 and outbound = 1

    if os.path.exists(newDir) == False:
        os.mkdir(newDir)

    with open(newDir + str(rat) + "_DATA.csv", 'w') as c:
        c.write("Session,Trial,Trial Type,Correct/Incorrect,Feeder #,Timestamp\n")

        for csv in files:
            lines = []
            if session == 15:
                break
            with open(dataDir + csv,'r') as f:
                data = f.readlines()
            for timestamp in data:
                if timestamp != data[0]:
                    lines.append(timestamp.split(','))
            for ln in lines:
                if type == 1:
                    if ln[1] == 'Correct':
                        c.write(str(session) + "," + str(trial) + ",Out,1," + ln[0] + "," + ln[2])
                    else:
                        c.write(str(session) + "," + str(trial) + ",Out,0," + ln[0] + "," + ln[2])
                else:
                    if ln[1] == 'Correct':
                        c.write(str(session) + "," + str(trial) + ",In,1," + ln[0] + "," + ln[2])
                    else:
                        c.write(str(session) + "," + str(trial) + ",In,0," + ln[0] + "," + ln[2])
                trial += 1
                if ln[0] == '2':
                    type = 1
                else:
                    type = 0

            session += 1
            trial = 1

for rat in rats:
    get_data(str(rat))

processedDir = baseDir + '/Processed Data/'

for rat in rats:
    data = pd.read_csv('{0}{1}/{1}_DATA.csv'.format(processedDir,str(rat)))
    inbound = data[data['Trial Type'] == 'In'][['Session','Correct/Incorrect']]
    outbound = data[data['Trial Type'] == 'Out'][['Session','Correct/Incorrect']]

    inbound.to_csv('{0}{1}/{1}_IN.csv'.format(processedDir,str(rat)))
    outbound.to_csv('{0}{1}/{1}_OUT.csv'.format(processedDir,str(rat)))

print "|||||||||||||||||Transformed Raw Data|||||||||||||||||"