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

#-outbound 0.01-10.0 0.01-1.0
#-inbound 0.01-10.0 0.01-1.0

def tinvlogit(x):
    import theano.tensor as t
    return t.exp(x) / (1 + t.exp(x))


###main code----------------------------------------------------

def main(group,anType,sessionNum):
    if group == 'Young':
        fig_no = 1
    else:
        fig_no = 2

    dir = '/Users/adelekap/Documents/WMaze_Analysis/Paper/data/'
    data_denom = pd.read_csv('{0}{1}Session/{2}{3}Denom.csv'.format(dir,str(sessionNum),anType,group))# csv of total trials for each day
    data_numAll = pd.read_csv('{0}{1}Session/{2}{3}Num.csv'.format(dir,str(sessionNum),anType,group)) # correct per day

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

    print('---------')
    (waic_val, waic_se, waic_p) = pm.stats.waic(model=model_old, trace=trace1, n_eff=True)
    dic_val = pm.stats.dic(model=model_old, trace=trace1)
    print('WAIC ', waic_val, '  DIC ', dic_val)
    print('---------')
    # plt.figure(50)
    # pm.traceplot(trace1, varnames=['sigmab', 'beta_0', 'sigma'])
    # plt.savefig('trace' + group + '.pdf')

    lt1 = {}
    for ii in range(len(data_numAll)):
        lc = 'p' + str(ii)
        summary_dataset = np.percentile(trace1[lc][:], [5, 50, 95], axis=0)
        # lt1[ii] = plot_results(np.asarray(summary_dataset), fig_no, ii + 1, group)

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
    with open('{0}{1}DATASET.txt'.format(group,anType), 'w') as data:
        data.write(str(np.asarray(summary_dataset)))
    # plot_results(np.asarray(summary_dataset), 3, 2, group)
    return trace1['p']




"""
----------------------------------------------------------------------
calls main twice - once for each group
"""

if __name__ == "__main__":
    """
    anType = Analysis Type {"overall", "inbound", "outbound"}
    """
    sessionNum = 21

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
    yng = main('Young', anType,sessionNum)
    old = main('Old', anType,sessionNum)

    p_bigger = yng - old
    prop_higher = pd.DataFrame()
    for t in range(p_bigger.shape[1]):
        prop_higher.set_value(t, 'prop', (p_bigger[:, t] > 0).sum() / float(p_bigger.shape[0]))

    r1 = np.reshape(yng, (1, yng.shape[0] * yng.shape[1]))
    r2 = np.reshape(old, (1, old.shape[0] * old.shape[1]))

    overall = ((r1 - r2) > 0).sum() / float(r1.shape[1])

    with open('{0}certainty.txt'.format(anType),'w') as c:
        c.write(str(prop_higher))

    print 'overall ', overall
    plt.figure(20)
    font = {'size': 17}
    matplotlib.rc('font', **font)
    matplotlib.rc('xtick', labelsize=15)
    matplotlib.rc('ytick', labelsize=15)
    plt.plot(prop_higher, lw=4)
    plt.title('Pr(Young > Old)')
    plt.ylabel('Certainty')
    plt.xlabel('Session')
    plt.axhline(0.95)
    plt.ylim(0,1)
    plt.savefig(anType + 'PrDiffBIN.pdf')

    rename(anType)

    print "|||||||||||||||||SESSION ANALYSIS COMPLETE|||||||||||||||||"
