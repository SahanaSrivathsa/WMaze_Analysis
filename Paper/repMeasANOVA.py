from numpy.random import normal
import pyvttbl as pt
from collections import namedtuple
from mean_SE import getData

# N = 40
# P = ["noise", "quiet"]
# rts = [998, 511]
# mus = rts * N
#
# Sub = namedtuple('Sub', ['Sub_id', 'rt','condition'])
# df = pt.DataFrame()
# for subid in xrange(0,N):
#     for i,condition in enumerate(P):
#         df.insert(Sub(subid+1,
#                      normal(mus[i], scale=112., size=1)[0],
#                            condition)._asdict())
# aov = df.anova('rt',sub='Sub_id',wfactors=['condition'])
# print aov


def create_data(data,age,s):
    ratIds = []
    props = []
    ages = []
    sessions = []
    for index, row in data.iterrows():
        n = len(row)
        ratIds = ratIds + [s+index for i in range(n)]
        sessions = sessions + range(1, n + 1)
        props = props + list(row)
        ages = ages + [age for j in range(n)]
    return ratIds,sessions,props,ages

def create_df(young,old,s):
    riYoung,sessYoung,propYoung,ageYoung = create_data(young,'young',0)
    riOld,sessOld,propOld,ageOld = create_data(old,'old',s)

    rat_ids = riYoung+riOld
    sessions = sessYoung +sessOld
    performance = propYoung+propOld
    ages = ageYoung + ageOld

    Sub = namedtuple('Sub', ['rat_id', 'Performance', 'Session', 'Age'])
    df = pt.DataFrame()
    for idx in xrange(len(riYoung + riOld)):
        df.insert(Sub(rat_ids[idx], performance[idx], sessions[idx], ages[idx])._asdict())

    return df

def extract_for_apa(factor, aov, values=['F', 'mse', 'eta', 'p']):
    results = {}
    for key, result in aov[(factor,)].iteritems():
        if key in values:
            results[key] = result

    return results

def repeated_measures_anova(trialType,sessionNum):
    young = getData(trialType,'young',sessionNum)
    old = getData(trialType,'old',sessionNum)
    df = create_df(young,old,len(young))
    aov = df.anova('Performance',sub='rat_id',wfactors=['Age','Session'])
    print(extract_for_apa('Age',aov))


repeated_measures_anova('inbound',14)
repeated_measures_anova('outbound',14)
repeated_measures_anova('inbound',21)
repeated_measures_anova('outbound',21r)

