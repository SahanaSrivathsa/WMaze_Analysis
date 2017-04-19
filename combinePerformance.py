import os

"""
This module takes the Timestamp files and creates a combined response txt file
to run through the state space analysis.
"""


rats = ['10348']
baseDir = "/Users/adelekap/Documents/W-Maze Raw/"


def get_data(rat):
    dataDir = baseDir + rat + "/TimeStamps/"
    files = os.listdir(dataDir)
    newDir = baseDir + rat + "Responses/"

    if os.path.exists(newDir) == False:
        os.mkdir(newDir)
        print "Creating new Directory"
    else:
        print "Directory already exists!"
    with open(newDir + str(rat) + "_combinedResponses.txt", 'w') as c:
        for csv in files:
            with open(dataDir + csv,'r') as f:
                rows = f.readlines()
            lines = []
            for timestamp in rows:
                if timestamp != rows[0]:
                    lines.append(timestamp.split(','))
            for line in lines:
                if line[1] == 'Correct':
                    c.write('1,')
                else:
                    c.write('0,')




for rat in rats:
    get_data(rat)