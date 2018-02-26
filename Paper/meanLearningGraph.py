import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def get_learning_sessions(age,trialNum,n):
    inFile = 'data/ssLearningTrials_{0}inbound{1}.txt'.format(age,trialNum)
    outFile = 'data/ssLearningTrials_{0}outbound{1}.txt'.format(age, trialNum)
    with open(inFile,'r') as i:
        inData = i.read().split(',')
    with open(outFile,'r') as o:
        outData = o.read().split(',')

    return [n+1 if x=='None' else int(x) for x in inData],[n+1 if y=='None' else int(y) for y in outData]

def make_dataframe(youngIn,youngOut,oldIn,oldOut):
    numY = len(youngIn)
    numO = len(oldIn)
    data = pd.DataFrame()
    data['Age'] = ['young' for i in range(numY * 2)] + ['old' for j in range(numO * 2)]
    data['Trial Type'] = ['Inbound' for k in range(numY)] + \
                           ['Outbound' for l in range(numY)] + \
                           ['Inbound' for m in range(numO)] + \
                           ['Outbound' for n in range(numO)]
    data['Learning Trial'] = youngIn + youngOut + oldIn + oldOut
    return data

youngIn14, youngOut14 = get_learning_sessions('young','14',14)
oldIn14, oldOut14 = get_learning_sessions('old','14',14)
data14 = make_dataframe(youngIn14,youngOut14,oldIn14,oldOut14)

youngIn21, youngOut21 = get_learning_sessions('young','21',21)
oldIn21, oldOut21 = get_learning_sessions('old','21',21)
data21 = make_dataframe(youngIn21,youngOut21,oldIn21,oldOut21)

colors = ['green','purple']

fig1, (ax1,ax2) = plt.subplots(1, 2,sharey=True)
ax1.set_ylim(1,16,2)
ax1.axhline(y=14,color='red')
ax2.axhline(y=14,color='red')

sns.boxplot(y='Learning Trial',x='Age',data=data14[data14['Trial Type']=='Inbound'],palette=sns.xkcd_palette(colors),
            width=0.6,ax=ax1)
sns.boxplot(y='Learning Trial',x='Age',data=data14[data14['Trial Type']=='Outbound'],palette=sns.xkcd_palette(colors),
            width=0.6,ax=ax2)
ax1.set_title('(a)')
ax2.set_title('(b)')
plt.yticks(range(1,15,1))
ax2.get_yaxis().set_visible(False)
plt.tight_layout()
plt.show()


fig2, (ax3,ax4) = plt.subplots(1, 2,sharey=True)
ax3.axhline(y=21,color='red')
ax4.axhline(y=21,color='red')
sns.boxplot(y='Learning Trial',x='Age',data=data21[data21['Trial Type']=='Inbound'],palette=sns.xkcd_palette(colors),
            width=0.6,ax=ax3)
sns.boxplot(y='Learning Trial',x='Age',data=data21[data21['Trial Type']=='Outbound'],palette=sns.xkcd_palette(colors),
            width=0.6,ax=ax4)
ax3.set_title('(c)')
ax4.set_title('(d)')
ax3.set_ylim(1,23,2)
plt.yticks(range(1,22,1))
ax4.get_yaxis().set_visible(False)
plt.tight_layout()
plt.show()


fig3, (ax5,ax6) = plt.subplots(1,2,figsize=(18,5))
data14N = data14
data14N['Learning Trial'] = ['Did Not \nLearn' if d==15 else d for d in data14N['Learning Trial']]
sns.countplot(x='Learning Trial',data=data14N[data14N['Trial Type']=='Inbound'],hue='Age',
              palette=sns.xkcd_palette(colors),order=range(1,15)+['Did Not \nLearn'],ax=ax5)
sns.countplot(x='Learning Trial',data=data14N[data14N['Trial Type']=='Outbound'],hue='Age',
              palette=sns.xkcd_palette(colors),order=range(1,15)+['Did Not \nLearn'],ax=ax6)
ax5.get_legend().set_visible(False)
ax6.get_legend().set_visible(False)
ax5.set_title('(a)')
ax6.set_title('(b)')
ax6.get_yaxis().label.set_visible(False)
ax5.set_ylim(0,11)
ax6.set_ylim(0,11)
ax5.tick_params(axis='both', which='major', labelsize=8)
ax6.tick_params(axis='both', which='major', labelsize=8)
plt.tight_layout()
plt.savefig('plots/14LearningSessions.pdf')
plt.show()

fig4, (ax7,ax8) = plt.subplots(1,2,figsize=(18,5))
data21N = data21
data21N['Learning Trial'] = ['Did Not \nLearn' if d==22 else d for d in data21N['Learning Trial']]
sns.countplot(x='Learning Trial',data=data21N[data21N['Trial Type']=='Inbound'],hue='Age',
              palette=sns.xkcd_palette(colors),order=range(1,22)+['Did Not \nLearn'],ax=ax7)
sns.countplot(x='Learning Trial',data=data21N[data21N['Trial Type']=='Outbound'],hue='Age',
              palette=sns.xkcd_palette(colors),order=range(1,22)+['Did Not \nLearn'],ax=ax8)
ax7.get_legend().set_visible(False)
ax8.get_legend().set_visible(False)
ax7.set_title('(c)')
ax8.set_title('(d)')
ax8.get_yaxis().label.set_visible(False)
ax7.set_ylim(0,5)
ax8.set_ylim(0,5)
ax7.tick_params(axis='both', which='major', labelsize=8)
ax8.tick_params(axis='both', which='major', labelsize=8)
plt.tight_layout()
plt.savefig('plots/21LearningSessions.pdf')
plt.show()
