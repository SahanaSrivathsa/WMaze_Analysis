import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from pymc3.distributions.timeseries import GaussianRandomWalk
from pylab import rcParams
import pymc3 as pm
import sys
import numpy as np
from scipy import stats
from renameFiles import *

"""
Random effects state space model
Anne Smith, April, 2017
Edits - Adele Kapellusch, July 2017
"""


def tinvlogit(x):
    import theano.tensor as t
    return t.exp(x) / (1 + t.exp(x))


# plotting -------------------------------------------

rcParams['figure.figsize'] = 15, 10
font = {'size': 16}
matplotlib.rc('font', **font)

def plot_results(fit, fig_no, sub_no, group):

    if group == 'Young':
        color = '#09933'
        dcolor = 'green'
        yv = 0.2
    else:
        color = 'purple'
        dcolor = '#9900cc'
        yv = 0.1

    plt.figure(fig_no)

    if fig_no < 3 and group == 'Young':
        plt.subplot(4,4,sub_no)
    elif fig_no <3 and group == 'Old':
        plt.subplot(4,3,sub_no)

    else:
        plt.subplot(1, 1, 1)


    plt.fill_between(np.arange(fit.shape[1]), fit[0, :], fit[2, :],
                     facecolor=color, alpha=0.5)
    if group == 'Young':
        plt.plot(fit[1, :], c=dcolor, alpha=1.0, lw=3, label='Young')
    else:
        plt.plot(fit[1, :], c=dcolor, alpha=1.0, lw=3, label='Old')

    plt.axhline(0.5, color='red', linestyle='-', label='chance = 0.5')

    last_time_below_threshold = np.where(fit[0, :] < 0.5)[-1]
    if not last_time_below_threshold.any():  # always above
        learning_trial = 1
    else:
        learning_trial = last_time_below_threshold[-1] + 2  # +2 to account for zero start and above line

    plt.xlabel('Session')
    plt.ylabel('Pr(correct)')
    plt.legend(loc='lower right', prop={'size': 10})
    plt.text(300, yv, group + ' learning session  ' + str(learning_trial))
    plt.ylim(0, 1.05)
    plt.xlim(0,14)
    plt.tight_layout()
    plt.savefig(group + str(fig_no) + '.pdf')
    return learning_trial


###main code----------------------------------------------------

def main(group,anType):
    if group == 'Young':
        fig_no = 1
    else:
        fig_no = 2

    dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'
    data_denom = pd.read_csv(dir + anType + group + 'Denom.csv')# csv of total trials for each day
    data_numAll = pd.read_csv(dir + anType + group + 'Num.csv') # correct per day

    numAnimals = len(data_numAll)

    with pm.Model() as model_old:
        sigma = pm.Uniform('sigma', float(sigmaMin), float(sigmaMax))
        sigmab = pm.Uniform('sigmab', float(sigmabMin), float(sigmabMax))

        betaPop0 = pm.Normal('betaPop0', mu=0, sd=100)
        beta_0 = pm.Normal('beta_0', mu=betaPop0, sd=sigmab, shape=len(data_numAll))

        x = GaussianRandomWalk('x', sd=sigma, init=pm.Normal.dist(mu=0.0, sd=0.01), shape=data_numAll.shape[1])
        pm.Deterministic('p', tinvlogit(x + betaPop0))

        for rat in range(numAnimals):
            stp = 'p{0}'.format(rat)
            stn = 'n{0}'.format(rat)
            pn = pm.Deterministic(stp, tinvlogit(x + beta_0[rat]))
            pm.Binomial(stn, p=pn, n=np.asarray(data_denom[rat:(rat+1)]), observed=np.asarray(data_numAll[rat:(rat+1)]))


    with model_old:
        step1 = pm.NUTS(vars=[x, sigmab, beta_0], gamma=.25)
        start2 = pm.sample(2000, step1)[-1]

        # Start next run at the last sampled position.
        step2 = pm.NUTS(vars=[x, sigmab, beta_0], scaling=start2, gamma=.55)
        trace1 = pm.sample(5000, step2, start=start2, progressbar=True)

    plt.figure(50)
    pm.traceplot(trace1, varnames=['sigmab', 'beta_0', 'sigma'])
    plt.savefig('trace' + group + '.pdf')

    lt1 = {}
    for ii in range(len(data_numAll)):
        lc = 'p' + str(ii)
        summary_dataset = np.percentile(trace1[lc][:], [5, 50, 95], axis=0)
        lt1[ii] = plot_results(np.asarray(summary_dataset), fig_no, ii + 1, group)

    if anType == 'overall':
        dtype = 'Overall'
    if anType == 'inbound':
        dtype = 'Inbound'
    if anType == 'outbound':
        dtype = 'Outbound'

    dataDir = '/Users/adelekap/Documents/WMaze_Analysis/StochasticVolatility/BySession/'
    txtFile = '{0}{1}Learning/{1}_{2}_learningTrials.txt'.format(dataDir,dtype,group)
    with open(txtFile , 'w') as learn:
        lts = lt1.values()
        for trial in lts:
            learn.write(str(trial)+'\n')
        learn.write("AVERAGE LEARNING TRIAL: "+ str(np.average(lts))+'\n')
        learn.write("STANDARD ERROR: "+ str(stats.sem(lts)))

    print "|||||||||||Completed Analysis for " + group + " data|||||||||||||"
    summary_dataset = np.percentile(trace1['p'], [5, 50, 95], axis=0)
    plot_results(np.asarray(summary_dataset), 3, 2, group)
    return trace1['p']




"""
----------------------------------------------------------------------
calls main twice - once for each group
"""

if __name__ == "__main__":
    """
    anType = Analysis Type {"overall", "inbound", "outbound"}
    """

    args = sys.argv[1:]
    anType = args[0][1:]

    sigmaMin,sigmaMax = args[1].split('-')
    sigmabMin,sigmabMax = args[2].split('-')

    print "||||||||||||Running model for " + anType + " data . . .||||||||||||||"
    print "SIGMA min: " + sigmaMin
    print "SIGMA max: " +sigmaMax
    print "SIGMAb min: "+ sigmabMin
    print 'SIGMAb max: '+ sigmabMax

    plt.close('all')
    p_sevo = main('Young',anType)
    p_oxyg = main('Old',anType)

    p_bigger = p_sevo - p_oxyg
    prop_higher = pd.DataFrame()
    for t in range(p_bigger.shape[1]):
        prop_higher.set_value(t, 'prop', (p_bigger[:, t] > 0).sum() / float(p_bigger.shape[0]))

    r1 = np.reshape(p_sevo, (1, p_sevo.shape[0] * p_sevo.shape[1]))
    r2 = np.reshape(p_oxyg, (1, p_oxyg.shape[0] * p_oxyg.shape[1]))

    overall = ((r1 - r2) > 0).sum() / float(r1.shape[1])

    print 'overall ', overall
    plt.figure(20)
    plt.plot(prop_higher, lw=2)
    plt.title('Pr(Young > Old)')
    plt.ylabel('Certainty')
    plt.xlabel('Session')
    plt.axhline(0.95)
    plt.savefig(anType + 'PrDiffBIN.pdf')

    rename(anType)

    print "|||||||||||||||||SESSION ANALYSIS COMPLETE|||||||||||||||||"
