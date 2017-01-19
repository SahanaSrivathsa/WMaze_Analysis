import os

#"All trials in which the rat departed either from the left
#food well or from the right food well were classified as inbound
#trials, and all trials in which the rat departed from the center food
#well were classified as outbound trials." - Loren,Frank (2009)

rats = ['10281','10282']
baseDir = "C:\\Users\\akoutia\\Documents\\Barnes Lab\\Wmaze\RatData\\"

def split_data(rat):
    dataDir = baseDir + rat + "\\TimeStamps\\"
    files = os.listdir(dataDir)
    newDir = baseDir + "Processed Data\\" + rat +"\\"
    session = 1
    trial = 1
    type = 0  #inbound = 0 and outbound = 1

    if os.path.exists(newDir) == False:
        os.mkdir(newDir)
        print "New Directory made"
    else:
        print "Directory already exists"
    with open(newDir + str(rat) + "_Outbound.csv", 'w') as c:
        c.write("Session,Trial,Correct/Incorrect,Feeder #\n")

        for csv in range (0,14):
            OutLines =[]
            with open(dataDir + files[csv],'r') as f:
                Outdata = f.readlines()
            for timestamp in Outdata:
                if timestamp != Outdata[0]:
                    OutLines.append(timestamp.split(','))
            for line in OutLines:
                if type == 1:
                    if line[1] == 'Correct':
                        c.write(str(session) + "," + str(trial) + ",1," + line[0] + "\n")
                    else:
                        c.write(str(session) + "," + str(trial) + ",0," + line[0] + "\n")
                    trial += 1
                if line[0] == '2':
                    type = 1
                if line [0] == '1' or line[0] == '3':
                    type = 0
            session += 1
        trial = 1
        session = 1


    with open(newDir + str(rat) + "_Inbound.csv", 'w') as c:
        c.write("Session,Trial,Correct/Incorrect,Feeder #\n")

        for csv in range(0,14):
            InLines = []
            with open(dataDir + files[csv], 'r') as f:
                Indata = f.readlines()
            for timestamp in Indata:
                if timestamp != Indata[0]:
                    InLines.append(timestamp.split(','))
            for line in InLines:
                if type == 0:
                    if line[1] == 'Correct':
                        c.write(str(session) + "," + str(trial) + ",1," + line[0] + "\n")
                    else:
                        c.write(str(session) + "," + str(trial) + ",0," + line[0] + "\n")
                    trial += 1
                if line[0] == '2':
                    type = 1
                if line [0] == '1' or line[0] == '3':
                    type = 0
            session += 1




for rat in rats:
    split_data(rat)