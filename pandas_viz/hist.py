import seaborn as sns
from df import *

dataframe = create_dataframe('/Volumes/ls 1/BarnesLab/RawData')

sns.set_style('whitegrid')

def plot_outbound_barplot():
    colors = ['#9658b7','#3b8437']
    sns.set_context(rc={"lines.linewidth":0.75})
    sns.barplot(x='Session',y='Outbound Errors',data = dataframe,hue='age',palette=colors,capsize=0.15)
    sns.plt.title('Outbound Errors by Session',fontsize=18)
    sns.plt.show()

def plot_inbound_barplot():
    colors = ['#9658b7','#3b8437']
    sns.barplot(x='Session',y='Inbound Errors',data = dataframe,hue='age',palette=colors,capsize=0.15)
    sns.plt.title('Inbound Errors by Session',fontsize=18)
    sns.plt.show()

plot_outbound_barplot()
plot_inbound_barplot()