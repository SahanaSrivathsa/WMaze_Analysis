import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from pylab import rcParams
from toArray import *

sigUp = 1.1
sigDown = 0.95



def plot_results(fit, fig_no, sub_no, group):
    font = {'size': 16}
    matplotlib.rc('font', **font)
    matplotlib.rc('xtick', labelsize=15)
    matplotlib.rc('ytick', labelsize=15)

    if group == 'Young':
        color = 'green'
        dcolor = '#006600'
        yv = 0.2
    else:
        color = '#9999ff'
        dcolor = 'purple'
        yv = 0.1

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
    plt.legend(loc='lower right', prop={'size': 15})
    plt.text(300, yv, group + ' learning session  ' + str(learning_trial))
    plt.ylim(0, 1.05)
    plt.xlim(1,float(sessionNum))
    plt.savefig(directory+group + str(fig_no) + '.pdf')


def ready_plot(yngData,oldData,certainty,anType,sessionNum,directory):
    plot_results(np.asarray(oldData), 3, 2, 'Old')
    plot_results(np.asarray(yngData), 3, 2, 'Young')
    plt.savefig(directory+anType+'Plot.pdf')
    plt.show()

    font = {'size': 17}

    matplotlib.rc('font', **font)
    matplotlib.rc('xtick', labelsize=15)
    matplotlib.rc('ytick', labelsize=15)
    plt.axhline(1.03,lw=50,color='r',alpha=0.35)
    plt.plot(range(1,int(sessionNum)+2),certainty, lw=3)
    plt.title('Pr(Young > Old)')
    plt.ylabel('Certainty')
    plt.xlabel('Session')
    plt.ylim(0,1.1)
    plt.xlim(1,int(sessionNum))
    plt.savefig(directory+anType+'PrDiffBIN.pdf')
    plt.show()


young_hSS = [hSS_y_in_14,hSS_y_out_14,hSS_y_in_21,hSS_y_out_21]
young_glm = [glm_y_in_14,glm_y_out_14,glm_y_in_21,glm_y_out_21]
old_hSS= [hSS_o_in_14,hSS_o_out_14,hSS_o_in_21,hSS_o_out_21]
old_glm = [glm_o_in_14,glm_o_out_14,glm_o_in_21,glm_o_out_21]
cert_hSS = [hSS_in_14_cert,hSS_out_14_cert,hSS_in_21_cert,hSS_out_21_cert]
cert_glm = [glm_in_14_cert,glm_out_14_cert,glm_in_21_cert,glm_out_21_cert]
strs = ['inbound','outbound','inbound','outbound']
sessionNums = ['14','14','21','21']




for i in range(4):
    sessionNum = sessionNums[i]
    directory = '/Users/adelekap/Documents/WMaze_Analysis/Paper/plots/hierarchicalSS/' + sessionNum + 'Sessions/'
    ready_plot(young_hSS[i],old_hSS[i],cert_hSS[i],strs[i],sessionNum,directory)


for j in range(4):
    sessionNum = sessionNums[j]
    directory = '/Users/adelekap/Documents/WMaze_Analysis/Paper/plots/glm/' + sessionNum + 'Sessions/'
    ready_plot(young_glm[j], old_glm[j], cert_glm[j], strs[j], sessionNum, directory)

# directory = '/Users/adelekap/Documents/WMaze_Analysis/Paper/plots/glm/' + sessionNum + 'Sessions/'