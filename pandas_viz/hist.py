import seaborn as sns
from df import *

dataframe = create_dataframe('/Volumes/ls 1/BarnesLab/RawData')
dataframe['Proportion Correct'] = dataframe['Correct']/dataframe['Total Feeder Visits']

trialTypeDataframe = trial_type_dataframe('/Volumes/ls 1/BarnesLab/RawData')

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


def plot_overall_barplot():
    colors = ['#9658b7', '#3b8437']
    sns.set_context(rc={"lines.linewidth": 0.75})
    sns.barplot(x='Session', y='Proportion Correct', data=dataframe, hue='age', palette=colors, capsize=0.15)
    sns.plt.title('Proportion Correct by Session', fontsize=16)
    sns.plt.show()

def plot_proportion_inbound():
    inbound = trialTypeDataframe[trialTypeDataframe['Trial Type'] == 'In'].reset_index()

    old_inb = inbound[inbound['Age'] == 'Old']
    young_inb = inbound[inbound['Age'] == 'Young']

    new_old = old_inb.groupby('Session')['Correct/Incorrect'].mean()
    new_young = young_inb.groupby('Session')['Correct/Incorrect'].mean()

    old_line = pd.DataFrame()
    old_line['Proportion'] = new_old
    old_line['Age'] = 'Old'

    young_line = pd.DataFrame()
    young_line['Proportion'] = new_young
    young_line['Age'] = 'Young'

    ln = pd.concat([old_line, young_line]).reset_index()
    sns.pointplot(x='Session', y='Proportion', hue='Age', data=ln)
    sns.plt.show()

def plot_proportion_outbound():
    #### NEEDS TO BE MODIFIED (no error bars)
    outbound = trialTypeDataframe[trialTypeDataframe['Trial Type'] == 'Out'].reset_index()

    old_out = outbound[outbound['Age'] == 'Old']
    young_out = outbound[outbound['Age'] == 'Young']

    new_old = old_out.groupby('Session')['Correct/Incorrect'].mean()
    new_young = young_out.groupby('Session')['Correct/Incorrect'].mean()

    old_line = pd.DataFrame()
    old_line['Proportion'] = new_old
    old_line['Age'] = 'Old'

    young_line = pd.DataFrame()
    young_line['Proportion'] = new_young
    young_line['Age'] = 'Young'

    ln = pd.concat([old_line, young_line]).reset_index()
    sns.pointplot(x='Session', y='Proportion', hue='Age', data=ln)
    sns.plt.ylim(0,1)
    sns.plt.show()

plot_proportion_outbound()


