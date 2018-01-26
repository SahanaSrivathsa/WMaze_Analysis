
def rename(t):
    import os

    if t == 'outbound':
        type = 'Outbound'
    if t == 'inbound':
        type = 'Inbound'
    if t == 'overall':
        type = 'Overall'

    baseDir = '/Users/adelekap/Documents/WMaze_Analysis/StochasticVolatility/BySession/'


    os.system("mv traceYoung.pdf {0}{1}Learning/{1}TraceYoungBIN.pdf".format(baseDir,type))
    os.system("mv Young1.pdf {0}{1}Learning/{1}IndivYoungBIN.pdf".format(baseDir,type))
    os.remove("Young3.pdf")

    os.system("mv traceOld.pdf {0}{1}Learning/{1}TraceOldBIN.pdf".format(baseDir, type))
    os.system("mv Old2.pdf {0}{1}Learning/{1}IndivOldBIN.pdf".format(baseDir, type))

    os.system("mv Old3.pdf {0}{1}Learning/{1}ComparisonBIN.pdf".format(baseDir,type))
    os.system("mv {0}PrDiffBIN.pdf {1}{0}Learning/{0}PrDiffBin.pdf".format(type,baseDir))
