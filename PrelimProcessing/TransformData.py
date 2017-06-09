import os

#"All trials in which the rat departed either from the left
#food well or from the right food well were classified as inbound
#trials, and all trials in which the rat departed from the center food
#well were classified as outbound trials." - Loren,Frank (2009)

"""This module takes the Timestamp files of the rats"""

with open('/Users/adelekap/Documents/WMaze_Analysis/pandas_viz/rats.csv', 'r') as rats:
    lns = rats.readlines()
rows = [line.split(',') for line in lns if line != lns[0]]

rats = [row[0] for row in rows]
rats.remove('10362')
baseDir = "/Volumes/ls 1/BarnesLab/RawData/"


def get_data(rat):
    dataDir = baseDir + rat + "/TimeStamps/"
    files = ['TimeStamps_{1}_Session{2}.csv'.format(baseDir,rat,session) for session in range(1,15)]
    newDir = baseDir + "Processed Data/" + rat +"/"
    session = 1
    trial = 1
    type = 0  #inbound = 0 and outbound = 1

    if os.path.exists(newDir) == False:
        os.mkdir(newDir)
        print "Creating new Directory"
    else:
        print "Directory already exists!"
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
    get_data(rat)