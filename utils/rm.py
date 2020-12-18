# simple rm in python supporting -r

import argparse, os, shutil

parser = argparse.ArgumentParser(description="Remove files with rm")
parser.add_argument("-r", action="store_true", help="Recursively remove files")
parser.add_argument("input", type=str, help="File you want to remove")

args = parser.parse_args()
input_arg = args.input

if args.r:
    shutil.rmtree(input_arg) # remove folder tree
else:
    if os.path.isfile(input_arg):
        os.remove(input_arg)
    else:
        print("Input {} is not a file".format(input_arg))
