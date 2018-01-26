

#State-space EM code in python
#Anne Smith 2015
import os
import glob
import csv
import pandas as pd
from   pylab import *
from   urllib import urlopen
from   datetime import datetime	
import matplotlib.pyplot as plt
import numpy as np
import sys
import math
from   operator import truediv
from   pandas.io.json import json_normalize
import pickle
import FiltersEM as ff
from   random import *

reload(ff)

def learningTrial(lowConf):
	current_session = 1
	for val in lowConf:
		if val > 0.5:
			return current_session
		else:
			current_session += 1
	return None


################################
def RunEM(df,sn,age,num,type,last=False):
	dir = '/Users/adelekap/Documents/WMaze_Analysis/Paper/plots/indivSS/{0}Sessions/{1}/{2}/'.format(str(sn),age,type)
	sigma2e    = 0.5**2 #start guess
	sigma_init = sigma2e
	p_init     = 0.5 #xx[0:2].mean()
	x_init     = 0.0

	if(p_init > 0.01 and p_init < 0.99):
		mu = np.log(p_init/(1-p_init))
	elif(p_init<=0.01):
		mu = -3.0
	else:
		mu = 3.0

	print sigma2e
	x_post,sigma2_post,sigma2e,sigma_init,converge_flag =  ff.EM(df.y, df.N, mu, sigma2e, x_init, sigma_init)
	
	print sigma2e
	pmode, p, pll, pul       = ff.TransformToProb(x_post, sigma2_post, mu)
	pmode = list(pmode)
	pmode = [pmode[0]]+pmode

	with open('/Users/adelekap/Documents/WMaze_Analysis/Paper/data/ssLearningTrials_'+age+type+str(sn)+'.txt','a') as w:
			w.write(str(learningTrial(pll))+',')

	# plt.plot([0, len(p)], [0.5, 0.5], 'k-', lw=1, alpha=0.9, color='red')
	if age == 'young':
		plt.plot(pmode,  linestyle = '-', color= 'green', alpha=0.63,lw=2)
	else:
		plt.plot(pmode, linestyle='-', color='purple', alpha=0.63, lw=2)

	plt.locator_params(axis = 'y', nbins = 3)
	plt.xlim(1,sn)
	plt.ylim(0,1)
	plt.xlabel('Session')
	plt.ylabel('Probability of Correct Response')
	if last:
		plt.plot([0, len(p)], [0.5, 0.5], 'k-', lw=1, alpha=0.9, color='red')
		plt.savefig(dir+'all_.pdf'.format(age))
		plt.show()
	return

###############################
def main(sessionNum,anType,group):
	df = pd.DataFrame()
	dir = '/Users/adelekap/Documents/WMaze_Analysis/Paper/data/'
	data_denom = pd.read_csv(
		'{0}{1}Session/{2}{3}Denom.csv'.format(dir, str(sessionNum), anType,
											   group))  # csv of total trials for each day
	animalNum = len(data_denom)
	data_denom = data_denom.transpose()
	data_numAll = pd.read_csv(
		'{0}{1}Session/{2}{3}Num.csv'.format(dir, str(sessionNum), anType, group)).transpose()  # correct per day
	for n in range(animalNum):
		tot_values = data_denom[n][1:]
		resp_values = data_numAll[n][1:]
		df['y'] = resp_values
		df['N'] = tot_values
		if n == animalNum-1 and group =='old':
			RunEM(df, sessionNum, group, n, anType, True)
		else:
			RunEM(df, sessionNum, group, n, anType)


		# RunEM(df,sessionNum,group,n,anType)


if __name__ == '__main__':
  main(14,'inbound','young')
  main(14,'inbound','old')
  main(14, 'outbound', 'young')
  main(14,'outbound','old')

  main(21, 'inbound', 'young')
  main(21, 'inbound', 'old')
  main(21, 'outbound', 'young')
  main(21, 'outbound', 'old')



