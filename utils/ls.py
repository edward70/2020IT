# basic ls in python

import os

cwd = os.getcwd() # get working directory
files = os.listdir(cwd) # list files in directory

for file in files:
    print(file) # print them all out
