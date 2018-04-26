#!/usr/bin/python3

from subprocess import call
import argparse
import fileinput
from os import remove
import platform
import re
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="UML file name")
parser.add_argument("-d","--depth", type=int, help="Anything after this depth will not be rendered", required=True)

args = parser.parse_args()

if not args.depth > 0:
    print("\n\tDepth must be greater than zero\n")
    exit(1)

for line in fileinput.input(args.file, inplace=1, backup='.bak'):
    line = re.sub('^\\t{{{}}}'.format(args.depth),"'", line.rstrip())
    print(line)

if not shutil.which("plantuml"):
    print("\n\tPlantUML not found, please install!\n")
    exit(1)

call(["plantuml", args.file])
image = args.file.rsplit(".", 1)[0] + '.png'

pl = platform.system()
if pl == "Linux":
    call(["eog", image])
elif pl == 'Darwin':
    call(["open", image])

# restore original file
shutil.move(args.file + '.bak', args.file)

# cleanup png
remove(image)
