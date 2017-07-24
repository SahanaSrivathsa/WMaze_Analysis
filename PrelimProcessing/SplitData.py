import os
import sys
import InboundGraphs
import OutboundGraphs

#"All trials in which the rat departed either from the left
#food well or from the right food well were classified as inbound
#trials, and all trials in which the rat departed from the center food
#well were classified as outbound trials." - Loren,Frank (2009)

"""
This module takes the Timestamp CSVs that are created at testting and splits them into
two csvs: inbound decisions and outbound decisions.

To run this, give the script the following command line arguments:
(1) List of rats you want to analyze separated by commas.
(2)The moving average trial number.
"""
rats = (sys.argv[1]).split(',')
# baseDir = "C:\\Users\\akoutia\\Documents\\Barnes Lab\\Wmaze\RatData\\"
baseDir = '/Volumes/TRANS 1/BarnesLab/RawData/'

def split_data(rat):
    dataDir = baseDir + rat + "/TimeStamps/"
    files = os.listdir(dataDir)
    newDir = baseDir + "Processed Data/" + rat +"/"
    session = 1
    trial = 1
    type = 0  #inbound = 0 and outbound = 1

    if os.path.exists(newDir) == False:
        os.mkdir(newDir)
        print "New Directory made"
    else:
        print "Directory already exists"
    with open(newDir + str(rat) + "_Outbound.csv", 'w') as c:
        c.write("Session,Trial,Correct/Incorrect,Feeder #\n")

        for csv in range (0,14):
            OutLines =[]
            with open(dataDir + files[csv],'r') as f:
                Outdata = f.readlines()
            for timestamp in Outdata:
                if timestamp != Outdata[0]:
                    OutLines.append(timestamp.split(','))
            for line in OutLines:
                if type == 1:
                    if line[1] == 'Correct':
                        c.write(str(session) + "," + str(trial) + ",1," + line[0] + "\n")
                    else:
                        c.write(str(session) + "," + str(trial) + ",0," + line[0] + "\n")
                    trial += 1
                if line[0] == '2':
                    type = 1
                if line [0] == '1' or line[0] == '3':
                    type = 0
            session += 1
        trial = 1
        session = 1


    with open(newDir + str(rat) + "_Inbound.csv", 'w') as c:
        c.write("Session,Trial,Correct/Incorrect,Feeder #\n")

        for csv in range(0,14):
            InLines = []
            with open(dataDir + files[csv], 'r') as f:
                Indata = f.readlines()
            for timestamp in Indata:
                if timestamp != Indata[0]:
                    InLines.append(timestamp.split(','))
            for line in InLines:
                if type == 0:
                    if line[1] == 'Correct':
                        c.write(str(session) + "," + str(trial) + ",1," + line[0] + "\n")
                    else:
                        c.write(str(session) + "," + str(trial) + ",0," + line[0] + "\n")
                    trial += 1
                if line[0] == '2':
                    type = 1
                if line [0] == '1' or line[0] == '3':
                    type = 0
            session += 1

def Trials(rat):
    INlines = []
    with open('{0}Processed Data/{1}/{1}_Inbound.csv'.format(baseDir,rat),'r') as inb:
        INdata = inb.readlines()
    for timestamp in INdata:
        if timestamp != INdata[0]:
            INlines.append(timestamp.split(','))
    inboundTrials = int(INlines[len(INlines) - 1][1])

    OUTlines = []
    with open('{0}Processed Data/{1}/{1}_Outbound.csv'.format(baseDir,rat),'r') as out:
        OUTdata = out.readlines()
    for timestamp in OUTdata:
        if timestamp != OUTdata[0]:
            OUTlines.append(timestamp.split(','))
    outboundTrials = int(OUTlines[len(OUTlines) - 1][1])

    return (inboundTrials,outboundTrials)

if __name__ == '__main__':
    for rat in rats:
        split_data(rat)
        trialNums = Trials(rat)
        InboundGraphs.execute(rat,trialNums[0],int(sys.argv[2]))
        OutboundGraphs.execute(rat,trialNums[1],int(sys.argv[2]))