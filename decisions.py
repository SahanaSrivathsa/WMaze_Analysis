"""
This module takes the inbound and outbound csvs and writes the results
of the decisions to a txt file.
The final product is two txt files with the inbound decisions and the outbound
decisions ready to import into the state space analysis.

ARGS:
    (1) list of rats to be analyzed separated by commas
    (2) directory of the rats' data
"""

import sys

def inbound_decisions(rat,directory):
    inputFile = '{0}{1}/{1}_Inbound.csv'.format(directory,rat)
    outputFile = '{0}{1}/{1}_InboundDecisions.txt'.format(directory,rat)
    with open(inputFile,'r') as csv:
        data = csv.readlines()

    lines = []

    for decision in data:
        if decision != data[0]:
            lines.append(decision.split(','))
    with open(outputFile,'w') as doc:
        for line in lines:
            if line == lines[len(lines) - 1]:
                doc.write(line[2])
            else:
                doc.write(line[2]+',')


def outbound_decisions(rat, directory):
    inputFile = '{0}{1}/{1}_Outbound.csv'.format(directory, rat)
    outputFile = '{0}{1}/{1}_OutboundDecisions.txt'.format(directory, rat)
    with open(inputFile, 'r') as csv:
        data = csv.readlines()

    lines = []

    for decision in data:
        if decision != data[0]:
            lines.append(decision.split(','))
    with open(outputFile, 'w') as doc:
        for line in lines:
            if line == lines[len(lines) - 1]:
                doc.write(line[2])
            else:
                doc.write(line[2] + ',')

if __name__ == '__main__':
    rats = sys.argv[1].split(',')
    dir = sys.argv[2]
    for rat in rats:
        inbound_decisions(rat,dir)
        outbound_decisions(rat,dir)