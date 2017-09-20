import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


"""
Plots the number of trials completed and the relative proportions of each trial type for
each age group.
"""

############### Getting data and formatting ######################
baseDir = "/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/"

inboundYoung = pd.read_csv(baseDir+'inboundYoungDenom.csv').T[1:]
outboundYoung = pd.read_csv(baseDir + 'outboundYoungDenom.csv').T[1:]
inboundOld = pd.read_csv(baseDir + 'inboundOldDenom.csv').T[1:]
outboundOld = pd.read_csv(baseDir + 'outboundOldDenom.csv').T[1:]

averages = pd.DataFrame()
averages['InboundYoung'] = inboundYoung.T.mean()
averages['OutboundYoung'] = outboundYoung.T.mean()
averages['InboundOld'] = inboundOld.T.mean()
averages['OutboundOld'] = outboundOld.T.mean()
averages['OutboundYoung'] = averages['InboundYoung'] + averages['OutboundYoung']
averages['OutboundOld'] = averages['InboundOld'] + averages['OutboundOld']


ages = ['Young' for i in range(14)] + ['Old' for j in range(14)]
inboundData = list(averages['InboundYoung'])+list(averages['InboundOld'])
outboundData = list(averages['OutboundYoung'])+list(averages['OutboundOld'])
updatedAverages = pd.DataFrame({
    'Session':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    'Age':ages,
    'Inbound':inboundData,
    'Outbound': outboundData
})

session = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

############### Plotting #############################
sns.set_style("white")
sns.set_context({"figure.figsize": (24, 10)})
colorPalOut =sns.diverging_palette(150, 275, s=80, l=40, n=2)
colorPalIn = sns.diverging_palette(150,275,s=80,l=60,n=2)

#Young
sns.barplot(x = 'Session', y = 'Outbound', hue='Age',data=updatedAverages,palette=colorPalOut)
bottom_plot = sns.barplot(x = 'Session', y = 'Inbound', hue='Age',data=updatedAverages,palette=colorPalIn)



#topbar = plt.Rectangle((0,0),1,1,fc="#004d00", edgecolor = 'none')
# bottombar = plt.Rectangle((0,0),1,1,fc='#39ac39',  edgecolor = 'none')
# l = plt.legend([bottombar, topbar], ['Inbound', 'Outbound'], loc=1, ncol = 2, prop={'size':16})
# l.draw_frame(False)

#Optional code - Make plot look nicer
sns.despine(left=True)
bottom_plot.set_ylabel("Number of Trials")
bottom_plot.set_xlabel("Session")

#Set fonts to consistent 16pt size
for item in ([bottom_plot.xaxis.label, bottom_plot.yaxis.label] +
             bottom_plot.get_xticklabels() + bottom_plot.get_yticklabels()):
    item.set_fontsize(16)

plt.show()