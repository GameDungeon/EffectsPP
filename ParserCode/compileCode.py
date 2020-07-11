import sys
import os
from parseClass import Parse

def execute():
    pass

def parse(txt):
    output = []
    txt = txt.replace("\n", "").split(";")
    print(txt)
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
    execute(files.pop(0))



if __name__ == "__main__":
    run()
