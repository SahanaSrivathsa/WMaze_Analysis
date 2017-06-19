

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

def  plot_results( data_numAll, data_denom, fit, fig_no, sub_no, group):
    
    data = data_numAll/data_denom
    if group == 'sevo':
        color = '#0073dd'
        dcolor = 'darkblue'
        yv = 0.2
    else:
        color = 'orange'
        dcolor = '#7f4b05'
        yv = 0.1
    plt.figure(fig_no)
    if fig_no < 3:
        plt.subplot(4,2,sub_no)
        t = range(data.shape[1])
        d = data[sub_no-1:sub_no].values.transpose()
        #plt.plot(t, d, 'darkgray', lw='0.001', marker='o',label='correct trials',markersize=3 )
        plt.plot(t, data[sub_no-1:sub_no].transpose().rolling(5, center=True).mean(), color=dcolor, lw=2, \
                 linestyle=':',label='MA(5)',markersize=3 )

    else:
        plt.subplot(1,1,1)
        t = range(data.shape[1])
        plt.plot(data.mean().rolling(5, center=True).mean(), color = dcolor ,linestyle = ':', \
                 lw=2, label='MA(5)')

    plt.fill_between( np.arange(fit.shape[1]), fit[0,:], fit[2,:], 
                         facecolor=color, alpha=0.5)
    if group == 'sevo':
        plt.plot( fit[1,:], c=dcolor, alpha=1.0, lw = 3, label='Sevo' )
    else:
        plt.plot( fit[1,:], c=dcolor, alpha=1.0, lw = 3, label='Oxygen' )
    
    
    plt.axhline( 0.5, color='red', linestyle='-', label='chance = 0.5' )
    
    #print fit[0,:]>0.5)
    last_time_below_threshold = np.where(fit[0,:]<0.5)[-1]
    if not last_time_below_threshold.any():  #always above
        learning_trial = 1
    else:    
        learning_trial = last_time_below_threshold[-1] + 2 #+2 to account for zero start and above line
    

    plt.xlabel('Trial')
    plt.ylabel('Pr(correct)')
    plt.legend(loc='lower right', prop={'size':4})
    plt.text(300,yv, group + ' learning trial  ' + str(learning_trial))
    plt.ylim(0,1.05)
    #plt.xlim(0,len(data_num)+0.25)
    plt.tight_layout()
    plt.savefig(group + str(fig_no) + '.png')
    return learning_trial

###main code----------------------------------------------------

def main(group, fig_no):


    if group == 'sevo':
        fig_no = 1
    else:
        fig_no = 2

    data_denom1  = pd.read_csv('MATLAB/' + group + '_denom.csv', header = None) # csv of total trials for each day
    data_numAll1 = pd.read_csv('MATLAB/' + group + '_num.csv', header = None)  # correct per day
    data_denom   = data_denom1[0:47].transpose() # 47 = number of days
    data_numAll  = data_numAll1[0:47].transpose()

    ct = -1

    with pm.Model() as model_old:


        #sigma   = pm.Exponential('sigma',  1, testval=.1)
        sigma   = pm.Uniform('sigma', 0.01, 0.2)
    
        #sigmab  = pm.Exponential('sigmab', 1, testval=.1) 
        sigmab  = pm.Uniform('sigmab', 0.2, 1.1)

        betaPop0 = pm.Normal('betaPop0', mu = 0, sd = 100)

        beta_0  = pm.Normal('beta_0', mu = betaPop0, sd=sigmab, shape = len(data_numAll))
        
        x  = GaussianRandomWalk('x', sd = sigma, init=pm.Normal.dist(mu=0.0, sd= 0.01),shape=data_numAll.shape[1])
        p  = pm.Deterministic( 'p',   tinvlogit(x + betaPop0) )

        p0 = pm.Deterministic( 'p0',  tinvlogit(x + beta_0[0] ) )
        p1 = pm.Deterministic( 'p1',  tinvlogit(x + beta_0[1] ) )
        p2 = pm.Deterministic( 'p2',  tinvlogit(x + beta_0[2] ) )
        p3 = pm.Deterministic( 'p3',  tinvlogit(x + beta_0[3] ) )
        p4 = pm.Deterministic( 'p4',  tinvlogit(x + beta_0[4] ) )
        p5 = pm.Deterministic( 'p5',  tinvlogit(x + beta_0[5] ) )
        p6 = pm.Deterministic( 'p6',  tinvlogit(x + beta_0[6] ) )
        p7 = pm.Deterministic( 'p7',  tinvlogit(x + beta_0[7] ) )

        n0 = pm.Binomial('n0', p=p0, n=np.asarray(data_denom[0:1]),  observed=np.asarray(data_numAll[0:1]))
        n1 = pm.Binomial('n1', p=p1, n=np.asarray(data_denom[1:2]),  observed=np.asarray(data_numAll[1:2]))
        n2 = pm.Binomial('n2', p=p2, n=np.asarray(data_denom[2:3]),  observed=np.asarray(data_numAll[2:3]))
        n3 = pm.Binomial('n3', p=p3, n=np.asarray(data_denom[3:4]),  observed=np.asarray(data_numAll[3:4]))
        n4 = pm.Binomial('n4', p=p4, n=np.asarray(data_denom[4:5]),  observed=np.asarray(data_numAll[4:5]))
        n5 = pm.Binomial('n5', p=p5, n=np.asarray(data_denom[5:6]),  observed=np.asarray(data_numAll[5:6]))
        n6 = pm.Binomial('n6', p=p6, n=np.asarray(data_denom[6:7]),  observed=np.asarray(data_numAll[6:7]))
        n7 = pm.Binomial('n7', p=p7, n=np.asarray(data_denom[7:8]),  observed=np.asarray(data_numAll[7:8]))

    with model_old:
        start = pm.find_MAP(vars=[x], fmin=optimize.fmin_l_bfgs_b)


    with model_old:
        step1  = pm.NUTS(vars=[x, sigmab, beta_0],scaling=start, gamma=.25)
        start2 = pm.sample(500, step1, start=start)[-1]

    # Start next run at the last sampled position.
        step2  = pm.NUTS(vars=[x,  sigmab, beta_0],scaling=start2, gamma=.55)
        trace1 = pm.sample(1000, step2, start=start2,  progressbar=True)
    

    plt.figure(50)
    fig = pm.traceplot(trace1, varnames=['sigmab', 'beta_0', 'sigma'])  
    plt.savefig('trace' + group + '.png')

#pm.summary(trace1,[p,beta_0])
#pm.gelman_rubin(trace1)
    lt1 ={}
    for ii in range(len(data_numAll)):
        lc = 'p' + str(ii)
        summary_dataset = np.percentile( trace1[lc][:], [5,50,95], axis=0 )
        lt1[ii] = plot_results( data_numAll, data_denom, np.asarray(summary_dataset), fig_no, ii+1, group)

    print group
    print lt1


    summary_dataset = np.percentile( trace1['p'], [5,50,95], axis=0 )
    ltgroup1        = plot_results( data_numAll, data_denom, np.asarray(summary_dataset), 3, 2, group)
    return  trace1['p']


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
    p_sevo   = main('sevo', 1)
    p_oxyg   = main('oxyg', 2)

    p_bigger = p_sevo-p_oxyg
    prop_higher = pd.DataFrame()
    for t in range(p_bigger.shape[1]):
        prop_higher.set_value(t,'prop', (p_bigger[:,t]>0).sum()/float(p_bigger.shape[0]))

    r1 = np.reshape(p_sevo, (1, p_sevo.shape[0]*p_sevo.shape[1]))
    r2 = np.reshape(p_oxyg, (1, p_oxyg.shape[0]*p_oxyg.shape[1]))

    overall = ((r1-r2)>0).sum()/float(r1.shape[1])

    print 'overall ', overall
    plt.figure(20)
    plt.plot(prop_higher, lw = 2)
    plt.title('Pr(Sevo > Oxygen)')
    plt.ylabel('Certainty')
    plt.xlabel('Trial')
    plt.axhline(0.95)
    plt.savefig('PrDiff.png')


