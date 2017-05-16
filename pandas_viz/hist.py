import seaborn as sns
from df import *

oldDFs, youngDFs = create_dataframes('/Volumes/ls 1/BarnesLab/RawData')

oldCon=pd.concat(oldDFs)
old = oldCon[oldCon['Session'] < 15]
old['age'] = 'Old'

youngCon = pd.concat(youngDFs)
young = youngCon[youngCon['Session'] < 15]
young['age'] = 'Young'

dataframe = pd.concat([old,young])

def plot_outbound_barplot():
    colors = ['purple','green']
    sns.barplot(x='Session',y='Outbound Errors',data = dataframe,hue='age',palette=colors)
    sns.plt.show()

def plot_inbound_barplot():
    colors = ['purple','green']
    sns.barplot(x='Session',y='Inbound Errors',data = dataframe,hue='age',palette=colors)
    sns.plt.show()

plot_outbound_barplot()
