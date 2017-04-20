

"""
This module takes the sessionInfo csvs and creates 4 traces:
young %inbound
old %inbound
young %outbound
old %outbound
"""

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

def percentOutbound(rat):
    data = getData(rat)
    totalErrors = [float(datapoint[9]) for datapoint in data if datapoint != data[0]]
    outboundErrors = [float(datapoint[6]) for datapoint in data if datapoint!= data[0]]
    percent =[]
    for i in range(len(totalErrors)):
        if totalErrors[i] == 0:
            percent.append(0)
        else:
            percent.append(round((outboundErrors[i]/totalErrors[i]),2))
    return percent

def percentInbound(rat):
    data = getData(rat)
    totalErrors = [float(datapoint[9]) for datapoint in data if datapoint != data[0]]
    inboundErrors = [float(datapoint[7]) for datapoint in data if datapoint!= data[0]]
    percent =[]
    for i in range(len(totalErrors)):
        if totalErrors[i] == 0:
            percent.append(0)
        else:
            percent.append(round((inboundErrors[i]/totalErrors[i]),2))
    for per in percent:
        if per > 1:
            print ("oh no!")
    return percent

def accumulateData(rats,mode):
    if mode == 'inbound':
        data = [percentInbound(rat) for rat in rats]
    if mode == 'outbound':
        data = [percentOutbound(rat) for rat in rats]
    return data

def createTrace(data):
    trace =[]
    for session in range(len(data[0])):
        sessionData = [data[rat][session] for rat in range(len(data))]
        trace.append(round(avg(sessionData),2))
    return trace





