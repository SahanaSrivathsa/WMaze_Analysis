import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from   pymc3.distributions.timeseries import GaussianRandomWalk
from   pylab import rcParams
import pymc3 as pm
from   scipy.sparse import csc_matrix
from   scipy import optimize
import sys

"""
Random effects state space model
Anne Smith, April, 2017
Edits - Adele Kapellusch, July 2017
"""


def tinvlogit(x):
    import theano.tensor as t
    return t.exp(x) / (1 + t.exp(x))


# plotting -------------------------------------------

rcParams['figure.figsize'] = 9, 7
font = {'size': 9}
matplotlib.rc('font', **font)


def plot_results(data_numAll, data_denom, fit, fig_no, sub_no, group):
    data = data_numAll / data_denom

    if group == 'Young':
        color = '#0073dd'
        dcolor = 'darkblue'
        yv = 0.2
    else:
        color = 'orange'
        dcolor = '#7f4b05'
        yv = 0.1

    plt.figure(fig_no)

    if fig_no < 3:
        plt.subplot(4, 3, sub_no)

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

    plt.xlabel('Trial')
    plt.ylabel('Pr(correct)')
    plt.legend(loc='lower right', prop={'size': 4})
    plt.text(300, yv, group + ' learning trial  ' + str(learning_trial))
    plt.ylim(0, 1.05)
    plt.tight_layout()
    plt.savefig(group + str(fig_no) + '.pdf')
    return learning_trial


###main code----------------------------------------------------

def main(group, fig_no):
    if group == 'Young':
        fig_no = 1
    else:
        fig_no = 2

    dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'
    data_denom = pd.read_csv(dir + 'overall' + group + 'Denom.csv').ix[:,:]  # csv of total trials for each day
    data_numAll = pd.read_csv(dir + 'overall' + group + 'Num.csv').ix[:,:]  # correct per day


    with pm.Model() as model_old:
        sigma = pm.Uniform('sigma', 0.1, 0.8)
        sigmab = pm.Uniform('sigmab', 0.1, 0.8)

        betaPop0 = pm.Normal('betaPop0', mu=0, sd=100)
        beta_0 = pm.Normal('beta_0', mu=betaPop0, sd=sigmab, shape=len(data_numAll))

        x = GaussianRandomWalk('x', sd=sigma, init=pm.Normal.dist(mu=0.0, sd=0.01), shape=data_numAll.shape[1])
        p = pm.Deterministic('p', tinvlogit(x + betaPop0))
        p0 = pm.Deterministic('p0', tinvlogit(x + beta_0[0]))
        p1 = pm.Deterministic('p1', tinvlogit(x + beta_0[1]))
        p2 = pm.Deterministic('p2', tinvlogit(x + beta_0[2]))
        p3 = pm.Deterministic('p3', tinvlogit(x + beta_0[3]))
        p4 = pm.Deterministic('p4', tinvlogit(x + beta_0[4]))
        p5 = pm.Deterministic('p5', tinvlogit(x + beta_0[5]))
        p6 = pm.Deterministic('p6', tinvlogit(x + beta_0[6]))
        p7 = pm.Deterministic('p7', tinvlogit(x + beta_0[7]))
        p8 = pm.Deterministic('p8', tinvlogit(x + beta_0[8]))
        p9 = pm.Deterministic('p9', tinvlogit(x + beta_0[9]))
        p10 = pm.Deterministic('p10', tinvlogit(x + beta_0[10]))
        p11 = pm.Deterministic('p11', tinvlogit(x + beta_0[11]))
        #p12 =pm.Deterministic( 'p12', tinvlogit(x + beta_0[12]) )

        n0 = pm.Binomial('n0', p=p0, n=np.asarray(data_denom[0:1]), observed=np.asarray(data_numAll[0:1]))
        n1 = pm.Binomial('n1', p=p1, n=np.asarray(data_denom[1:2]), observed=np.asarray(data_numAll[1:2]))
        n2 = pm.Binomial('n2', p=p2, n=np.asarray(data_denom[2:3]), observed=np.asarray(data_numAll[2:3]))
        n3 = pm.Binomial('n3', p=p3, n=np.asarray(data_denom[3:4]), observed=np.asarray(data_numAll[3:4]))
        n4 = pm.Binomial('n4', p=p4, n=np.asarray(data_denom[4:5]), observed=np.asarray(data_numAll[4:5]))
        n5 = pm.Binomial('n5', p=p5, n=np.asarray(data_denom[5:6]), observed=np.asarray(data_numAll[5:6]))
        n6 = pm.Binomial('n6', p=p6, n=np.asarray(data_denom[6:7]), observed=np.asarray(data_numAll[6:7]))
        n7 = pm.Binomial('n7', p=p7, n=np.asarray(data_denom[7:8]), observed=np.asarray(data_numAll[7:8]))
        n8 = pm.Binomial('n8', p=p8, n=np.asarray(data_denom[8:9]), observed=np.asarray(data_numAll[8:9]))
        n9 = pm.Binomial('n9', p=p9, n=np.asarray(data_denom[9:10]), observed=np.asarray(data_numAll[9:10]))
        n10 = pm.Binomial('n10', p=p10, n=np.asarray(data_denom[10:11]), observed=np.asarray(data_numAll[10:11]))
        n11 = pm.Binomial('n11', p=p11, n=np.asarray(data_denom[11:12]), observed=np.asarray(data_numAll[11:12]))
        #n12 = pm.Binomial('n12', p=p12, n=np.asarray(data_denom[12:13]), observed=np.asarray(data_numAll[12:13]))


    with model_old:
        step1 = pm.NUTS(vars=[x, sigmab, beta_0], gamma=.25)
        start2 = pm.sample(500, step1)[-1]

        # Start next run at the last sampled position.
        step2 = pm.NUTS(vars=[x, sigmab, beta_0], scaling=start2, gamma=.55)
        trace1 = pm.sample(1000, step2, start=start2, progressbar=True)

    plt.figure(50)
    fig = pm.traceplot(trace1, varnames=['sigmab', 'beta_0', 'sigma'])
    plt.savefig('trace' + group + '.pdf')

    lt1 = {}
    for ii in range(len(data_numAll)):
        lc = 'p' + str(ii)
        summary_dataset = np.percentile(trace1[lc][:], [5, 50, 95], axis=0)
        lt1[ii] = plot_results(data_numAll, data_denom, np.asarray(summary_dataset), fig_no, ii + 1, group)

    print group
    print lt1

    summary_dataset = np.percentile(trace1['p'], [5, 50, 95], axis=0)
    ltgroup1 = plot_results(data_numAll, data_denom, np.asarray(summary_dataset), 3, 2, group)
    return trace1['p']


"""
----------------------------------------------------------------------
calls main twice - once for each group
plots stuff
"""

if __name__ == "__main__":

    if len(sys.argv) != 1:
        print 'usage: runBothBin.py'
        sys.exit(1)

    plt.close('all')
    p_sevo = main('Young', 1)
    p_oxyg = main('Old', 2)

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
    plt.savefig('PrDiffBIN.pdf')
