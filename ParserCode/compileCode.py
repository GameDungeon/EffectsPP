import ctypes  # An included library with Python install.
import sys
import os


from EffectsPP.ParserCode.parseClass import Parse

def write(lines):
    with open("creatures.txt", "a") as f:
        f.write(lines)

def execute(file):
    parse = Parse()
    output = []

    for line in file:
        i = 0
        while i < len(line):
            if line[i] in parse.funcList:
                if line[i] in parse.DiffCall.keys():
                    line[i] = parse.DiffCall[line[i]]
                #try:
                i = getattr(Parse, line[i])(parse, line, i)
                #except Exception as e:
                #    error(f"Error:{e}, form line {' '.join(line)}")
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


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def error(error):
    Mbox("Error", error, 0)
    sys.exit() 

def clearFiles():
    with open("creatures.txt", "w") as f:
        f.write("")


def run():
    clearFiles() #clears output file
    files = readFiles() #reads code
    execute(files.pop(0)) #executes creatures.txt



if __name__ == "__main__":
    run()
