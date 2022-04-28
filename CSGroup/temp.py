import os
import sys

import pandas as pd

path = 'C:\\Users\\chai8\\Downloads\\TweepyWork\\CollectedDataset\\'

dir_items = os.listdir(path)

rows = 0

for item in dir_items:

    isdir = os.path.isdir(path + item)

    if isdir:
        files = os.listdir(path+item)


        for file in files:

            numrows = pd.read_csv(path+item+'\\'+file, lineterminator='\n', skiprows=1, header=None).shape[0]

            rows += numrows

            print(f'{file} is {numrows} cumulative {rows}')

