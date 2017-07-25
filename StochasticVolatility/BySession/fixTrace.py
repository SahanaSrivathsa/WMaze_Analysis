dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'
denomFiles = [dir+'inboundOldDenom.csv',dir+'outboundOldDenom.csv',dir+'inboundYoungDenom.csv',dir+'outboundYoungDenom.csv',
              dir+'overallOldDenom.csv',dir+'overallYoungDenom.csv']
numFiles = [dir+'inboundOldNum.csv',dir+'outboundOldNum.csv',dir+'inboundYoungNum.csv',dir+'outboundYoungNum.csv',
            dir+'overallOldNum.csv',dir+'overallYoungNum.csv']


def runFix(fileList,type):
    if type == 'd':
        value = '10'
    else:
        value = '5'

    for f in fileList:
        with open(f,'r') as read:
            lines = read.readlines()

        with open(f ,'w') as write:
            write.write('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14\n')

            for line in lines:
                if line != lines[0]:
                    write.write(value + ',' + line[6:])


runFix(denomFiles,'d')
runFix(numFiles,'n')
