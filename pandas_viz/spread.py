from df import *
import pandas as pd
import numpy as np
import cufflinks as cf
import plotly.offline as offline
import plotly.graph_objs as go

cf.go_offline()

dataframe = create_dataframe('/Volumes/ls 1/BarnesLab/RawData')

# oldBool = dataframe['age'] == 'Old'
# youngBool = dataframe['age'] == 'Young'


def mean_out(bool):
    sess_group = dataframe[bool].groupby('Session')
    mean = sess_group.mean()
    return mean

yngOut = mean_out(dataframe['age'] == 'Young').reset_index()
oldOut = mean_out(dataframe['age'] == 'Old').reset_index()

yngOut.columns = ['Session','yng Correct','yng Initial Error','yng Outbound Errors','yng Inbound Errors','yng Repeat Errors',
                  'yng Total Errors','yng Total Feeder Visits']
oldOut.columns = ['Session','old Correct','old Initial Error','old Outbound Errors','old Inbound Errors','old Repeat Errors',
                  'old Total Errors','old Total Feeder Visits']

combo = yngOut.merge(oldOut, on='Session')

data = combo[['yng Outbound Errors','old Outbound Errors']]




