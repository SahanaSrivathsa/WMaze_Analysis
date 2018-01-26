from scipy.stats import mstats
import numpy as np

def get_data(age,sn,type):
    with open('/Users/adelekap/Documents/WMaze_Analysis/Paper/data/ssLearningTrials_{0}{1}{2}.txt'.format(age,type,sn),
              'r') as r:
        data = [x for x in r.read().split(',') if x != '']
        lts = [float(sn) if y=='None' else float(y) for y in data]
    # print(type+age+str(sn))
    # print(np.mean(lts))
    # print(np.std(lts))
    return lts

print('INBOUND 14')
print(mstats.ttest_ind(get_data('young',14,'inbound'),get_data('old',14,'inbound')))

print('OUTBOUND 14')
print(mstats.ttest_ind(get_data('young',14,'outbound'),get_data('old',14,'outbound')))

print('INBOUND 21')
print(mstats.ttest_ind(get_data('young',21,'inbound'),get_data('old',21,'inbound')))

print('OUTBOUND 21')
print(mstats.ttest_ind(get_data('young',21,'outbound'),get_data('old',21,'outbound')))

