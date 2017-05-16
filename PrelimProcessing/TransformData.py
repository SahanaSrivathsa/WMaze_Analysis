import os

#"All trials in which the rat departed either from the left
#food well or from the right food well were classified as inbound
#trials, and all trials in which the rat departed from the center food
#well were classified as outbound trials." - Loren,Frank (2009)

"""This module takes the Timestamp files of the rats"""


rats = ['10348']
baseDir = "C:\\Users\\akoutia\\Documents\\Barnes Lab\\Wmaze\RatData\\"


def get_data(rat):
    dataDir = baseDir + rat + "\\TimeStamps\\"
    files = os.listdir(dataDir)
    newDir = baseDir + "Processed Data\\" + rat +"\\"
    lines = []
    session = 1
    trial = 1
    type = 0  #inbound = 0 and outbound = 1

    if os.path.exists(newDir) == False:
        os.mkdir(newDir)
        print "Creating new Directory"
    else:
        print "Directory already exists!"
    with open(newDir + str(rat) + "_DATA.csv", 'w') as c:
        c.write("Session,Trial,Trial Type,Correct/Incorrect,Feeder #,Timestamp\n")

        for csv in files:
            if session == 15:
                break
            with open(dataDir + csv,'r') as f:
                data = f.readlines()
            for timestamp in data:
                if timestamp != data[0]:
                    lines.append(timestamp.split(','))
            for line in lines:
                if type == 1:
                    if line[1] == 'Correct':
                        c.write(str(session) + "," + str(trial) + ",Out,1," + line[0] + "," + line[2])
                    else:
                        c.write(str(session) + "," + str(trial) + ",Out,0," + line[0] + "," + line[2])
                else:
                    if line[1] == 'Correct':
                        c.write(str(session) + "," + str(trial) + ",In,1," + line[0] + "," + line[2])
                    else:
                        c.write(str(session) + "," + str(trial) + ",In,0," + line[0] + "," + line[2])
                trial += 1
                if line[0] == '2':
                    type = 1
                else:
                    type = 0

            session += 1
            trial = 1



for rat in rats:
    get_data(rat)