#!/usr/bin/python

from subprocess import call
import argparse
import fileinput
from os import remove
import re
from shutil import move

parser = argparse.ArgumentParser()
parser.add_argument("file", help="UML file name")
parser.add_argument("-d","--depth",help="Anything after this depth will not be rendered")

args = parser.parse_args()

for line in fileinput.input(args.file, inplace=1, backup='.bak'):
    line = re.sub('^\\t{{{}}}'.format(args.depth),"'", line.rstrip())
    print(line)

call(["plantuml", args.file])
image = args.file.rsplit(".", 1)[0] + '.png'
call(["eog",image])

# restore original file
move(args.file + '.bak', args.file)

# cleanup png
remove(image)
