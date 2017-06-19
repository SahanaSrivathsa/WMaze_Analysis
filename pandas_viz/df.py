import pandas as pd


def get_rats():
    with open('rats.csv','r') as rats:
        lines = rats.readlines()
    rows = [line.split(',') for line in lines if line != lines[0]]

    oldRats = [row[0] for row in rows if int(row[1]) == 25]
    youngRats = [row[0] for row in rows if int(row[1]) == 10]
    return (oldRats,youngRats)


def create_dataframe(rawDataDir):

    oldRats,youngRats = get_rats()

    oldDataframes = [pd.read_csv('{0}/{1}/SessionInfo_{1}.csv'.format(rawDataDir,rat))[['Session','Session Length','Correct','Initial Error','Outbound Errors','Inbound Errors',
                     'Repeat Errors','Total Errors','Total Feeder Visits']] for rat in oldRats]
    youngDataframes = [pd.read_csv('{0}/{1}/SessionInfo_{1}.csv'.format(rawDataDir,rat))[['Session','Session Length','Correct','Initial Error','Outbound Errors','Inbound Errors',
                     'Repeat Errors','Total Errors','Total Feeder Visits']] for rat in youngRats]
    oldCon=pd.concat(oldDataframes)
    old = oldCon[oldCon['Session'] < 15]
    old['age'] = 'Old'

    youngCon = pd.concat(youngDataframes)
    young = youngCon[youngCon['Session'] < 15]
    young['age'] = 'Young'

    return pd.concat([old,young])


def updateDF(df,rat,age):
    df['Rat'] = rat
    df['Age'] = age

       
def trial_type_dataframe(rawDataDir):
    oldRats,youngRats = get_rats()

    oldDataframes = []
    youngDataframes = []

    for rat in oldRats:
        df = pd.read_csv('{0}/Processed Data/{1}/{1}_DATA.csv'.format(rawDataDir,rat))
        df['Rat'] = rat
        df['Age'] = 'Old'
        df = df[df['Session'] < 15]
        oldDataframes.append(df)

    for rat in youngRats:
        df = pd.read_csv('{0}/Processed Data/{1}/{1}_DATA.csv'.format(rawDataDir,rat))
        df['Rat'] = rat
        df['Age'] = 'Young'
        df = df[df['Session'] < 15]
        youngDataframes.append(df)

    old = pd.concat(oldDataframes)
    young = pd.concat(youngDataframes)

    return pd.concat((old,young))














