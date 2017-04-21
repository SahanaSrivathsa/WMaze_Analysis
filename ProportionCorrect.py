"""
This module takes the timestamp CSVs and creates
plots of proportion correct for young and old populations
"""
import numpy as np

workingDir = "/Users/adelekap/Documents/BarnesLab/RawData/"

youngRats = [10279,10280,10348,10349]
oldRats = [10281,10282,10351,10353,10354]

def avg(list):
    sum = 0
    for num in list:
        sum += num
    return sum/len(list)

def getData(rat):
    sessionFile = workingDir + str(rat) +'/SessionInfo_'+str(rat)+'.csv'
    with open(sessionFile,'r') as input:
        lines = input.readlines()

    data = [line.split(',') for line in lines]
    return data

def percentCorrect(rat):
    data = getData(rat)
    totalErrors = [float(datapoint[9]) for datapoint in data if datapoint != data[0]]
    totalCorrect = [float(datapoint[4]) for datapoint in data if datapoint!= data[0]]
    percent =[]
    for i in range(len(totalErrors)):
        if totalErrors[i] == 0:
            percent.append(0)
        else:
            percent.append(round(totalCorrect[i]/(totalCorrect[i]+totalErrors[i]),2))
    return percent


def accumulateData(rats):
    data = [percentCorrect(rat) for rat in rats]
    return data


def errorBars(rats):
    data = accumulateData(rats)
    STDVs = []
    for session in range(len(data[0])): #CHANGE IF NOT JUST DOING 14 SESSIONS!
        sessionData = [data[rat][session] for rat in range(len(data))]
        STDVs.append(round(np.std(sessionData),2))
    return STDVs


def createProportionTrace(data):
    trace =[]
    for session in range(len(data[0])):
        sessionData = [data[rat][session] for rat in range(len(data))]
        trace.append(round(avg(sessionData),2))
    return trace





