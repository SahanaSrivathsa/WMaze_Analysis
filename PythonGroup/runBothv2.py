

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from  pymc3.distributions.timeseries import GaussianRandomWalk
from  pylab import rcParams
import pymc3 as pm
from   scipy.sparse import csc_matrix
from   scipy import optimize
import sys

"""
Random effects state space model
Anne Smith, April, 2017

: run the code in the terminal window with
: "python runBoth.py"
: requires package: pymc3

"""

def tinvlogit(x):
    import theano.tensor as t
    return t.exp(x) / (1 + t.exp(x))


#plotting -------------------------------------------

rcParams['figure.figsize'] = 9, 7
font = { 'size'   : 9}
matplotlib.rc('font', **font)

def plot_results( data, fit, fig_no, sub_no, group):
    
    if group == 'young':
        color = '#0073dd'
        dcolor = 'darkblue'
        yv = 0.2
    else:
        color = 'orange'
        dcolor = '#7f4b05'
        yv = 0.1
    plt.figure(fig_no)
    if fig_no < 3:
        plt.subplot(4,3,sub_no)
        t = range(data.shape[1])
        d = data[sub_no-1:sub_no].values.transpose()
        #plt.plot(t, d, 'darkgray', lw='0.001', marker='o',label='correct trials',markersize=3 )
        plt.plot(t, data[sub_no-1:sub_no].transpose().rolling(30, center=True).mean(), color=dcolor, lw=2, \
                 linestyle=':',label='MA(30)',markersize=3 )

    else:
        plt.subplot(1,1,1)
        t = range(data.shape[1])
        plt.plot(data.mean().rolling(30, center=True).mean(), color = dcolor ,linestyle = ':', \
                 lw=2, label='MA(30)')

    plt.fill_between( np.arange(fit.shape[1]), fit[0,:], fit[2,:], 
                         facecolor=color, alpha=0.5)
    if group == 'young':
        plt.plot( fit[1,:], c=dcolor, alpha=1.0, lw = 3, label='Young' )
    else:
        plt.plot( fit[1,:], c=dcolor, alpha=1.0, lw = 3, label='Old' )
    
    
    plt.axhline( 0.5, color='red', linestyle='-', label='chance = 0.5' )
    
    #print fit[0,:]>0.5)
    last_time_below_threshold = np.where(fit[0,:]<0.5)[-1]
    if not last_time_below_threshold.any():  #always above
        learning_trial = 1
    else:    
        learning_trial = last_time_below_threshold[-1] + 2 #+2 to account for zero start and above line
    

    plt.xlabel('Trial')
    plt.ylabel('Pr(correct)')
    plt.legend(loc='upper right', prop={'size':4})
    plt.text(300,yv, group + ' learning trial  ' + str(learning_trial))
    plt.ylim(0,1.05)
    #plt.xlim(0,len(data_num)+0.25)
    plt.tight_layout()
    plt.savefig(group + str(fig_no) + '.png')
    return learning_trial

###main code----------------------------------------------------

def main(group, fig_no, savetrace):


    if group == 'young':
        fig_no = 1
    else:
        fig_no = 2

    data_numAll = pd.read_csv('/Volumes/TRANS 1/datanew.csv')
    data_numAll = data_numAll.ix[:11,1:100]

    ratNums = pd.read_csv('/Users/adelekap/Documents/WMaze_Analysis/pandas_viz/rats.csv')
    

    ct = -1

    with pm.Model() as model_old:

        #sigma   = pm.Exponential('sigma',  1, testval=.1)
        sigma   = pm.Uniform('sigma', 0.02, 0.5)
    
        #sigmab  = pm.Exponential('sigmab', 1, testval=.1) 
        sigmab  = pm.Uniform('sigmab', 0.01,0.7)

        beta_0  = pm.Normal('beta_0', 0., sd=sigmab, shape = len(data_numAll))
   
        x  = GaussianRandomWalk('x', sd = sigma, init=pm.Normal.dist(mu=0.0, sd=100.0),shape=data_numAll.shape[1])
        p  = pm.Deterministic( 'p',  tinvlogit(x) )
        p0 = pm.Deterministic( 'p0',  tinvlogit(x + beta_0[0] ) )
        p1 = pm.Deterministic( 'p1',  tinvlogit(x + beta_0[1] ) )
        p2 = pm.Deterministic( 'p2',  tinvlogit(x + beta_0[2] ) )
        p3 = pm.Deterministic( 'p3',  tinvlogit(x + beta_0[3] ) )
        p4 = pm.Deterministic( 'p4',  tinvlogit(x + beta_0[4] ) )
        p5 = pm.Deterministic( 'p5',  tinvlogit(x + beta_0[5] ) )
        p6 = pm.Deterministic( 'p6',  tinvlogit(x + beta_0[6] ) )
        p7 = pm.Deterministic( 'p7',  tinvlogit(x + beta_0[7] ) )
        p8 = pm.Deterministic( 'p8',  tinvlogit(x + beta_0[8] ) )
        p9 = pm.Deterministic('p9', tinvlogit(x + beta_0[9]))
        p10 = pm.Deterministic('p10', tinvlogit(x + beta_0[10]))
        p11 = pm.Deterministic('p11', tinvlogit(x + beta_0[11]))

        n0 = pm.Bernoulli('n0', p=p0,  observed=np.asarray(data_numAll[0:1]))
        n1 = pm.Bernoulli('n1', p=p1,  observed=np.asarray(data_numAll[1:2]))
        n2 = pm.Bernoulli('n2', p=p2,  observed=np.asarray(data_numAll[2:3]))
        n3 = pm.Bernoulli('n3', p=p3,  observed=np.asarray(data_numAll[3:4]))
        n4 = pm.Bernoulli('n4', p=p4,  observed=np.asarray(data_numAll[4:5]))
        n5 = pm.Bernoulli('n5', p=p5,  observed=np.asarray(data_numAll[5:6]))
        n6 = pm.Bernoulli('n6', p=p6,  observed=np.asarray(data_numAll[6:7]))
        n7 = pm.Bernoulli('n7', p=p7,  observed=np.asarray(data_numAll[7:8]))
        n8 = pm.Bernoulli('n8', p=p8, observed=np.asarray(data_numAll[8:9]))
        n9 = pm.Bernoulli('n9', p=p9, observed=np.asarray(data_numAll[9:10]))
        n10 = pm.Bernoulli('n10', p=p10, observed=np.asarray(data_numAll[10:11]))
        n11 = pm.Bernoulli('n11', p=p7, observed=np.asarray(data_numAll[11:12]))

    # with model_old:
    #     start = pm.find_MAP(vars=[x, sigmab, sigma, beta_0], fmin=optimize.fmin_l_bfgs_b)


    with model_old:
        step1  = pm.NUTS(vars=[x, sigmab, sigma, beta_0], gamma=.25)
        start2 = pm.sample(1000, step1)[-1]

    # Start next run at the last sampled position.
        step2  = pm.NUTS(vars=[x,  sigmab, sigma, beta_0],scaling=start2, gamma=.55)
        trace1 = pm.sample(2000, step2, start=start2,  progressbar=True)
    

    plt.figure(50)
    fig = pm.traceplot(trace1, varnames=['sigmab', 'beta_0','sigma'])  
    plt.savefig('trace' + group + '.png')

#pm.summary(trace1,[p,beta_0])
#pm.gelman_rubin(trace1)
    savetrace[group] = trace1
    lt1 ={}
    for ii in range(len(data_numAll)):
        lc = 'p' + str(ii)
        summary_dataset = np.percentile( trace1[lc][:], [5,50,95], axis=0 )
        lt1[ii] = plot_results( data_numAll, np.asarray(summary_dataset), fig_no, ii+1, group)

    print group
    print lt1


    sx1 = trace1['x'].shape[0]
    sx2 = trace1['x'].shape[1]
    betas_dist = trace1['sigmab'].mean() * np.random.randn(sx1,sx2)
    newx = trace1['x'] + betas_dist
    p    = np.exp(newx)/(1+np.exp(newx))

    summary_dataset = np.percentile( p, [5,50,95], axis=0 )
    ltgroup1        = plot_results( data_numAll, np.asarray(summary_dataset), 3, 2, group)
    return p


"""
----------------------------------------------------------------------
calls main twice - once for each group
plots stuff

"""

if __name__ == "__main__":

    if len(sys.argv) != 1:
        print 'usage: runBoth.py'
        sys.exit(1)

    plt.close('all')
    savetrace = {}
    p_sevo   = main('young', 1, savetrace)
    p_oxyg   = main('old', 2, savetrace)
    #
    # p_bigger = p_sevo-p_oxyg
    # prop_higher = pd.DataFrame()
    # for t in range(p_bigger.shape[1]):
    #     prop_higher.set_value(t,'prop', (p_bigger[:,t]>0).sum()/float(p_bigger.shape[0]))
    #
    # r1 = np.reshape(p_sevo, (1, p_sevo.shape[0]*p_sevo.shape[1]))
    # r2 = np.reshape(p_oxyg, (1, p_oxyg.shape[0]*p_oxyg.shape[1]))
    #
    # overall = ((r1-r2)>0).sum()/float(r1.shape[1])
    #
    # print 'overall ', overall
    # plt.figure(20)
    # plt.plot(prop_higher, lw = 2)
    # plt.title('Pr(Sevo > Oxygen)')
    # plt.ylabel('Certainty')
    # plt.xlabel('Trial')
    # plt.axhline(0.95)
    # plt.savefig('PrDiff.png')


