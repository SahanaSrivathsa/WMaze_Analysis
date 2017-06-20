import pandas as pd

df = pd.read_csv('/Users/adelekap/Documents/WMaze_Analysis/pandas_viz/rats.csv')
oldRats = list(df[df['AGE'] == 25]['RAT'])
youngRats = list(df[df['AGE'] == 10]['RAT'])

dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'

# for rat in rats:
#     with open('{0}{1}/{1}_DATA.csv'.format(dir,str(rat)),'r') as input:
#         lines = input.readlines()
#     rows = [line.split(',') for line in lines]
#     with open('{0}{1}/{1}_IN.csv'.format(dir,str(rat)),'w') as outputIn:
#         outputIn.write('Session,Correct/Incorrect\n')
#         with open('{0}{1}/{1}_OUT.csv'.format(dir,str(rat)),'w') as outputOut:
#             outputOut.write('Session,Correct/Incorrect\n')
#             for row in rows:
#                 if row[2] == 'In':
#                     outputIn.write(row[0]+','+row[3]+'\n')
#                 if row[2] == 'Out':
#                     outputOut.write(row[0]+','+row[3]+'\n')
inboundOld = pd.DataFrame()
inboundYoung = pd.DataFrame()
outboundOld = pd.DataFrame()
outboundYoung = pd.DataFrame()

directory = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'
for rat in youngRats:
    inboundYoung[rat] = pd.read_csv(directory+str(rat)+'/'+str(rat)+
                               '_IN.csv')['Correct/Incorrect']
    outboundYoung[rat] = pd.read_csv(directory + str(rat) + '/' + str(rat) +
                               '_OUT.csv')['Correct/Incorrect']
for rat in oldRats:
    inboundOld[rat] = pd.read_csv(directory+str(rat)+'/'+str(rat)+
                               '_IN.csv')['Correct/Incorrect']
    outboundOld[rat] = pd.read_csv(directory + str(rat) + '/' + str(rat) +
                               '_OUT.csv')['Correct/Incorrect']

inboundOldnew = inboundOld.transpose()
inboundYoungnew = inboundYoung.transpose()
outboundOldnew = outboundOld.transpose()
outboundYoungnew = outboundYoung.transpose()


inboundOldnew.to_csv(directory+'inOld.csv')
inboundYoungnew.to_csv(directory+'inYoung.csv')
outboundOldnew.to_csv(directory+'outOld.csv')
outboundYoungnew.to_csv(directory+'outYoung.csv')

