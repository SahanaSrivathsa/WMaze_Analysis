import pymc3 as pm
import pandas as pd
import numpy as np

sigmaMin = 0.1
sigmaMax = 0.8
sigmabMin = 0.1
sigmabMax = 0.8

anType = 'inbound'
group ='Young'

dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'
inYoung = pd.read_csv(dir+'inboundYoungDenom.csv')

with pm.Model() as h_model:
    mu_a = pm.Normal('mu_a', mu=0., sd=100 ** 2)
    sigma_a = pm.HalfCauchy('sigma_a', 5)
    mu_b = pm.Normal('mu_b', mu=0., sd=100 ** 2)
    sigma_b = pm.HalfCauchy('sigma_b', 5)
    a = pm.Normal('a', mu=mu_a, sd=sigma_a, shape=n_counties)
    # Intercept for each county, distributed around group mean mu_a
    b = pm.Normal('b', mu=mu_b, sd=sigma_b, shape=n_counties)