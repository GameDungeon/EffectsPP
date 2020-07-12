import sys
import os

from EffectsPP.ParserCode.parseClass import Parse

def write(lines):
    with open("creatures.txt", "w") as f:
        f.write(lines)

def execute(file):
    parse = Parse()
    output = []
    for line in file:
        i = 0
        while i < len(line):
            if line[i] in parse.funcList:
                i = getattr(Parse, line[i])(parse, line, i)
            else:
                i+=1
            
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
