#!/bin/bash

python /Users/adelekap/Documents/WMaze_Analysis/PrelimProcessing/TransformData.py

python /Users/adelekap/Documents/WMaze_Analysis/StochasticVolatility/BySession/createPropCSV.py

python /Users/adelekap/Documents/WMaze_Analysis/StochasticVolatility/BySession/fixTrace.py

python /Users/adelekap/Documents/WMaze_Analysis/StochasticVolatility/BySession/runBothBin.py $*


