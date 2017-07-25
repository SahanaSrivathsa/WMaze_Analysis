import os

dir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/PRE'
newdir = '/Volumes/TRANS 1/BarnesLab/RawData/Processed Data/'

denomFiles = [dir+'inboundOldDenom.csv',dir+'outboundOldDenom.csv',dir+'inboundYoungDenom.csv',dir+'outboundYoungDenom.csv',
              dir+'overallOldDenom.csv',dir+'overallYoungDenom.csv']
numFiles = [dir+'inboundOldNum.csv',dir+'outboundOldNum.csv',dir+'inboundYoungNum.csv',dir+'outboundYoungNum.csv',
            dir+'overallOldNum.csv',dir+'overallYoungNum.csv']
denomFilesNew = [newdir+'inboundOldDenom.csv',newdir+'outboundOldDenom.csv',newdir+'inboundYoungDenom.csv',newdir+'outboundYoungDenom.csv',
              newdir+'overallOldDenom.csv',newdir+'overallYoungDenom.csv']
numFilesNew = [newdir+'inboundOldNum.csv',newdir+'outboundOldNum.csv',newdir+'inboundYoungNum.csv',newdir+'outboundYoungNum.csv',
            newdir+'overallOldNum.csv',newdir+'overallYoungNum.csv']


def runFix(fileList,type,newFileList):
    if type == 'd':
        value = '10'
    else:
        value = '5'

    for index in range(len(fileList)):
        with open(fileList[index],'r') as read:
            lines = read.readlines()

        with open(newFileList[index],'w') as write:
            write.write('0,1,2,3,4,5,6,7,8,9,10,11,12,13,14\n')

            for line in lines:
                if line != lines[0]:
                    write.write(value + ',' + line[6:])
        os.remove(fileList[index])


runFix(denomFiles,'d',denomFilesNew)
runFix(numFiles,'n',numFilesNew)

print "||||||||||||||||Cleaned up Session Data|||||||||||||||"