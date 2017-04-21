
"""
Takes Timestamps CSVs and makes traces for time spent at
center feeder preceding correct and incorrect trials for
both old and young.
"""

import numpy as np
import datetime

workingDir = "/Users/adelekap/Documents/BarnesLab/RawData/"

youngRats = [10279,10280,10348,10349]
oldRats = [10281,10282,10351,10353,10354]

def avg(list):
    sum = 0
    for num in list:
        sum += num
    return sum/len(list)

def convertTime(timeArray):
    mins = int(timeArray[0])
    secs = int(timeArray[1])
    return (mins*60)+secs

def timeDiff(t1,t2):
    later = t2.split(':')
    earlier = t1.split(':')
    difference = convertTime(later) - convertTime(earlier)
    return difference


def times(rat,mode):
    #CHANGE SESSION RANGE IF MORE THAN 14 SESSIONS!!!
    files = [('{0}{1}/TimeStamps/TimeStamps_{1}_Session{2}.csv'.format(workingDir,str(rat),session)) for session in range(1,15)]
    avg_times = []
    for f in files:
        sessionTimes = []
        with open(f,'r') as ts:
            lines = ts.readlines()
        data = [line.split(',') for line in lines]
        for row in range(len(data)-1):
            if mode =='c':
                if data[row][0] == '2' and data[row+1][1] == 'Correct':
                    sessionTimes.append(timeDiff(data[row][2],data[row+1][2]))
            if mode =='i':
                if data[row][0] == '2' and data[row+1][1] != 'Correct':
                    sessionTimes.append(timeDiff(data[row][2],data[row+1][2]))
        avg_times.append(avg(sessionTimes))
    return avg_times

def accumulateData(rats,mode):
    data = [times(rat,mode) for rat in rats]
    return data


def errorBars(rats,mode):
    data = accumulateData(rats,mode)
    STDVs = []
    for session in range(len(data[0])): #CHANGE IF NOT JUST DOING 14 SESSIONS!
        sessionData = [data[rat][session] for rat in range(len(data))]
        STDVs.append(round(np.std(sessionData),2))
    return STDVs


def createTimeTrace(data):
    trace =[]
    for session in range(len(data[0])):
        sessionData = [data[rat][session] for rat in range(len(data))]
        trace.append(round(avg(sessionData),2))
    return trace