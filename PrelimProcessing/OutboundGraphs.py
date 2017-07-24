import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def execute(rat,trials,avg):
    plot_results(rat,prep_data(rat,trials,avg),trials,avg)

def prep_data(rat,trialNum,movAvg):
    baseDir = "/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/" + rat + "/"
    inboundCSV = baseDir + rat +"_Outbound.csv"
    with open(inboundCSV,'r') as ic:
        data = ic.readlines()
        lines = []
        for row in data:
            lines.append(row.split(','))
    correct = []
    for line in lines:
        if line != lines[0]:
            correct.append(float(line[2]))
    percentages = []

    for i in range(movAvg,trialNum,movAvg):
        percent = float(sum(correct[(i-10):i]))/10.0
        percentages.append(round(percent,3))
    return percentages

def plot_results(rat,proportions,trialNum,movAvg):
    baseDir = "/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/" + rat + "/"
    trials = range(movAvg,trialNum,movAvg)

    figureName = baseDir + rat + "_OutboundTrials.png"
    fig = plt.figure(rat)
    plt.scatter(trials,proportions)
    plt.plot(trials,proportions)
    plt.axis([1,trialNum,0,1])
    plt.title(rat)
    plt.xlabel("Cumulative Count of Outbound Trials")
    plt.ylabel("Proportion Correct in " + str(movAvg) + "-trial moving window")
    plt.savefig(figureName)
    plt.show()
    plt.close()



if __name__ == '__main__':
    execute()











