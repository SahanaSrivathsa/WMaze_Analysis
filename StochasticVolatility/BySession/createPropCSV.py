import pandas as pd

df = pd.read_csv('/Users/adelekap/Documents/WMaze_Analysis/pandas_viz/rats.csv')
oldRats = list(df[df['AGE'] == 25]['RAT'])
youngRats = list(df[df['AGE'] == 10]['RAT'])

dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'

def BySession(rat):
    data = pd.read_csv('{0}{1}/{1}_DATA.csv'.format(dir,str(rat)))
    return (data.groupby(['Session']).count()['Correct/Incorrect'],data.groupby(['Session']).sum()['Correct/Incorrect'])

def Inbound(rat):
    inboundData = pd.read_csv('{0}{1}/{1}_IN.csv'.format(dir,str(rat)))
    return (inboundData.groupby(['Session']).count()['Correct/Incorrect'],inboundData.groupby(['Session']).sum()['Correct/Incorrect'])

def Outbound(rat):
    outboundData = pd.read_csv('{0}{1}/{1}_OUT.csv'.format(dir,str(rat)))
    return (outboundData.groupby(['Session']).count()['Correct/Incorrect'],outboundData.groupby(['Session']).sum()['Correct/Incorrect'])

overallYngDenom = pd.DataFrame()
inboundYngDenom = pd.DataFrame()
outboundYngDenom = pd.DataFrame()
overallOldDenom = pd.DataFrame()
inboundOldDenom = pd.DataFrame()
outboundOldDenom = pd.DataFrame()

overallYngCorrect = pd.DataFrame()
inboundYngCorrect = pd.DataFrame()
outboundYngCorrect = pd.DataFrame()
overallOldCorrect = pd.DataFrame()
inboundOldCorrect = pd.DataFrame()
outboundOldCorrect = pd.DataFrame()


for rat in youngRats:
    test = BySession(rat)[0]
    test2 = BySession(rat)[1]
    overallYngDenom[str(rat)],overallYngCorrect[str(rat)] = BySession(rat)
    inboundYngDenom[str(rat)],inboundYngCorrect[str(rat)] = Inbound(rat)
    outboundYngDenom[str(rat)],outboundYngCorrect[str(rat)] = Outbound(rat)

for oldRat in oldRats:
    overallOldDenom[str(oldRat)],overallOldCorrect[str(oldRat)] = BySession(oldRat)
    inboundOldDenom[str(oldRat)],inboundOldCorrect[str(oldRat)] = Inbound(oldRat)
    outboundOldDenom[str(oldRat)],outboundOldCorrect[str(oldRat)] = Outbound(oldRat)


overallYngDenom.transpose().to_csv(dir+'PREoverallYoungDenom.csv')
overallYngCorrect.transpose().to_csv(dir+'PREoverallYoungNum.csv')
inboundYngDenom.transpose().to_csv(dir+'PREinboundYoungDenom.csv')
inboundYngCorrect.transpose().to_csv(dir+'PREinboundYoungNum.csv')
outboundYngDenom.transpose().to_csv(dir+'PREoutboundYoungDenom.csv')
outboundYngCorrect.transpose().to_csv(dir+'PREoutboundYoungNum.csv')


overallOldDenom.transpose().to_csv(dir+'PREoverallOldDenom.csv')
overallOldCorrect.transpose().to_csv(dir+'PREoverallOldNum.csv')
inboundOldDenom.transpose().to_csv(dir+'PREinboundOldDenom.csv')
inboundOldCorrect.transpose().to_csv(dir+'PREinboundOldNum.csv')
outboundOldDenom.transpose().to_csv(dir+'PREoutboundOldDenom.csv')
outboundOldCorrect.transpose().to_csv(dir+'PREoutboundOldNum.csv')

print "|||||||||||||||||Created Session Data|||||||||||||||||"










