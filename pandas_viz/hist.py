import seaborn as sns
from df import *
import matplotlib.pyplot as plt

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


def plot_trialType_proportions(type):
    colors = ['#9658b7', '#3b8437']
    if type == 'Outbound':
        df = trialTypeDataframe[trialTypeDataframe['Trial Type'] == 'Out'].reset_index()
        title = 'Proportion Correct Outbound by Session'
    if type == 'Inbound':
        df = trialTypeDataframe[trialTypeDataframe['Trial Type'] == 'In'].reset_index()
        title = 'Proportion Correct Inbound by Session'

    old = df[df['Age'] == 'Old']
    young = df[df['Age'] == 'Young']
    con = pd.concat([old,young])

    print 'Plotting data for {0} rats: {1} Young and {2} Old'.format(con['Rat'].nunique(),con[con['Age'] == 'Young']['Rat'].nunique(),
                                                                     con[con['Age'] == 'Old']['Rat'].nunique())

    ax = sns.pointplot(x='Session', y='Correct/Incorrect',hue='Age',data=con,palette=colors,capsize=0.1,errwidth=1.5)
    plt.setp(ax.collections, sizes=[40])
    sns.plt.ylim(0,1)
    sns.plt.title(title,fontsize=16)
    sns.plt.ylabel('Proportion Correct {0} Decisions'.format(type),fontsize=12)
    sns.plt.xlabel('Session',fontsize=12)
    sns.plt.savefig('{0}Proportion.pdf'.format(type))
    sns.plt.show()

def plot_overall_proportions():
    colors = ['#9658b7', '#3b8437']
    df = trialTypeDataframe
    title = 'Task Performance Across Sessions'
    old = df[df['Age'] == 'Old']
    young = df[df['Age'] == 'Young']
    con = pd.concat([old, young])

    print 'Plotting data for {0} rats: {1} Young and {2} Old'.format(con['Rat'].nunique(),
                                                                     con[con['Age'] == 'Young']['Rat'].nunique(),
                                                                     con[con['Age'] == 'Old']['Rat'].nunique())
    ax = sns.pointplot(x='  Session', y='Correct/Incorrect', hue='Age', data=con, palette=colors, capsize=0.1, errwidth=1.5)
    plt.setp(ax.collections, sizes=[40])
    sns.plt.ylim(0, 1)
    sns.plt.title(title, fontsize=16)
    sns.plt.ylabel('Proportion Correct', fontsize=12)
    sns.plt.xlabel('Session', fontsize=12)
    sns.plt.savefig('OverallPerformance.pdf')
    sns.plt.show()

plot_trialType_proportions('Inbound')
plot_trialType_proportions('Outbound')
plot_overall_proportions()






