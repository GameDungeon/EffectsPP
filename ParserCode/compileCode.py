import sys
import os
from parseClass import Parse

def command(line, i):
    parse = Parse()
    if line[i] in parse.funcList:
        out = getattr(Parse, line[i])()

def execute(line):
    i = 0
    output = []
    while i < len(line):
        i, out = command(line, i)
        output.append(out)
    

def parse(txt):
    output = []
    txt = txt.replace("\n", "").split(";")

    for line in txt:
        output.append(line.split(" "))

    while([""] in output):
        output.remove([""])

    return output

def readFiles():
    files = []

    with open("EffectsPP\code\Epp_creatures.txt") as f:
        files.append(parse(f.read()))

    return files

def run():
    files = readFiles()
    execute(files.pop(0)) #executes creatures.txt



if __name__ == "__main__":
    run()
