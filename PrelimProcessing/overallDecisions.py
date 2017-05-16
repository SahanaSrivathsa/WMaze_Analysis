decisions =[]
for f in range(1,15):
    with open('/Users/adelekap/Documents/BarnesLab/RawData/10282/TimeStamps/TimeStamps_10282_Session'+
                      str(f)+'.csv', 'r') as fi:
        lines = fi.readlines()
        data = [line.split(',') for line in lines]
        for d in data:
            if d[1] == 'Type':
                pass
            if d[1] == 'Correct':
                decisions.append('1')
            else:
                decisions.append('0')

with open('/Users/adelekap/Documents/10282.txt', 'w') as out:
    for d in decisions:
        out.write(d+',')
