import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

"""
(1) Change the list 'rats' to a list of all the rats that need data to be analyzed.
(2) Change the int 'trialNum' to be the number of trials to analyze over.
(3) Change the int 'movAvg' to be the moving average trial number. (A 10 trial moving average would be movAvg = 10)
"""

rats = ['10281','10282']
trialNum = 560
movAvg = 20

def prep_data(rat):
    baseDir = "C:\\Users\\akoutia\\Documents\\Barnes Lab\\Wmaze\RatData\\Processed Data\\" + rat + "\\"
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

def plot_results(rat,proportions):
    baseDir = "C:\\Users\\akoutia\\Documents\\Barnes Lab\\Wmaze\RatData\\Processed Data\\" + rat + "\\"
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


for rat in rats:
    plot_results(rat,prep_data(rat))










