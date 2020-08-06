import ctypes 
import sys
import os
from ast import literal_eval
from pathlib import Path


class Manager():
    def __init__(self):
        super().__init__()

        self.util = Util(self)

        self.FileM = FileManager(self)
        self.Func = Functions(self)

        self.FileM.readFiles()
        self.FileM.clearFiles()  # clears output file

        self.execute(self.FileM.files.pop(0))  # executes creatures.txt

    def execute(self, file):
        for line in file:
            i = 0
            while i < len(line):
                self.Func.runFunc(line, i)

class FileManager():
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

    def write(self, lines):
        with open(str(Path(os.path.dirname(os.path.realpath(__file__))).parent.parent) + "\creatures.txt", "a") as f:
            f.write(lines)

    def clearFiles(self):
        with open(str(Path(os.path.dirname(os.path.realpath(__file__))).parent.parent) + "\creatures.txt", "w") as f:
            f.write("")

    def readFiles(self):
        self.files = []
        with open(str(Path(os.path.dirname(os.path.realpath(__file__))).parent) + "\code\Epp_creatures.txt") as f:
            self.files.append(self.parseLine(f.read()))

    def parseLine(self, txt):
        output = []
        txt = txt.replace("\n", "").split(";")

        for line in txt:
            output.append(line.split(" "))

        while([""] in output):
            output.remove([""])

        return output

class Util():
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.DiffCall = {'=': "equal"}

    def getCall(self, func):
        if func in self.DiffCall.keys():
            return self.DiffCall[func]
        else:
            return func

    def Mbox(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    def error(self, error):
        self.Mbox("Error", error, 0)
        sys.exit()        

class Functions():
    def __init__(self, manager):
        super().__init__()
        self.funcList = ['new', '=']
        self.var = {"Null": None}
        self.manager = manager

    ###Utility Functions For Functions
    def useVars(self, perams):
        return str(tuple(perams[1:-1].split(",")))

    def setVar(self, varName, varValue):
        self.var[varName] = varValue

    def runFunc(self, line, i):
        if line[i] in self.funcList:
            line[i] = Util.getCall(line[i])
            try:
                i, output = getattr(self, line[i])(line, i)
            except Exception as e:
                self.manager.util.error(
                    f"Error:{e}, from line {' '.join(line)}")
        else:
            self.manager.util.error(f"No Function, from line {' '.join(line)}")

    ###Functions

    def equal(self, line, i):
        self.setVar(line[i-1], line[i+1])
        return i+2, None

    def new(self, line, i):
        if line[i + 1][:8] == "Creature":
            creature = eval("Creature" + self.useVars(line[i+1][8:]))
            Compile.write(creature.text())
            return i+2, None

        compileCode.error(f'''Imporper New Value on line: 
        {" ".join(line)}''')

class Template():
    pass

def run():
    manager = Manager()

if __name__ == "__main__":
    run()
