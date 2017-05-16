import pandas as pd


def create_dataframes(rawDataDir):

    with open('rats.csv','r') as rats:
        lines = rats.readlines()
    rows = [line.split(',') for line in lines if line != lines[0]]

    oldRats = [row[0] for row in rows if int(row[1]) == 25]
    youngRats = [row[0] for row in rows if int(row[1]) == 10]

    oldRats = ['10426','10425','10427','10422','10424','10281','10282','10351','10353','10354']
    youngRats = ['10416','10348','10349','10279','10280']

    oldDataframes = [pd.read_csv('{0}/{1}/SessionInfo_{1}.csv'.format(rawDataDir,rat))[['Session','Session Length','Correct','Initial Error','Outbound Errors','Inbound Errors',
                     'Repeat Errors','Total Errors','Total Feeder Visits']] for rat in oldRats]
    youngDataframes = [pd.read_csv('{0}/{1}/SessionInfo_{1}.csv'.format(rawDataDir,rat))[['Session','Session Length','Correct','Initial Error','Outbound Errors','Inbound Errors',
                     'Repeat Errors','Total Errors','Total Feeder Visits']] for rat in youngRats]

    return (oldDataframes,youngDataframes)








