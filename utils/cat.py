# cat in python

import os, sys

if len(sys.argv) > 1: # check if arguments exist
    filename = sys.argv[1]
    if os.path.isfile(filename): # check if argument is a file
        with open(filename) as f: # open file
            print(f.read()) # print file contents
    else:
        print("Error: {} is not a file".format(filename))
