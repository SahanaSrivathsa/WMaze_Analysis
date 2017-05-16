workingDir = "/Users/adelekap/Documents/BarnesLab/RawData/"

youngRats = [10348,10349]
oldRats = [10351,10353,10354]

def fix(rat):
    fi = workingDir + str(rat) + '/SessionInfo_' + str(rat) + '.csv'
    with open(fi,'r') as input:
        lines = input.readlines()
    rows = [line.split(',') for line in lines]

    with open(fi,'w') as output:
        for row in rows:
            output.write(
                '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}'.format(row[0], row[1], row[2], row[3], row[4],
                                                                             row[6], row[7], row[8], row[9],
                                                                             row[10], row[11], row[12]))


fix(10349)
fix(10351)
fix(10353)
fix(10354)