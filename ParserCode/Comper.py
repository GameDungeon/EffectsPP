import ctypes 
import sys
import os
from ast import literal_eval
import pathlib

"""Initialises other classes, and serves as a connector between them"""
class Manager():
    def __init__(self):
        super().__init__()

        self.util = Util(self)
        self.FileM = FileManager(self)
        self.Func = Functions(self)

        self.FileM.readFiles()
        self.FileM.clearFiles()

        self.execute(self.FileM.files.pop(0)) 

    def execute(self, file):
        for line in file:
            i = 0
            while i < len(line):
                i = self.Func.runFunc(line, i)

"""Loads/Writes to most of the EPP files"""
class FileManager():
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

    def write(self, lines):
        with open(str(pathlib.Path(__file__).parent.absolute().parent.parent) + "\creatures.txt", "a") as f:
            f.write(lines)

    def clearFiles(self):
        with open(str(pathlib.Path(__file__).parent.absolute().parent.parent) + "\creatures.txt", "w") as f:
            f.write("")

    def readFiles(self):
        self.files = []
        with open(str(pathlib.Path(__file__).parent.absolute().parent) + "\code\Epp_creatures.txt") as f:
            self.files.append(self.parseLine(f.read()))

    def parseLine(self, txt):
        output = []
        txt = txt.replace("\n", "").split(";")

        for line in txt:
            output.append(line.split(" "))

        while([""] in output):
            output.remove([""])

        return output

"""Holder general utility functions used by all classes"""
class Util():
    def __init__(self, manager):
        super().__init__()
        self.manager = manager

    def Mbox(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    def error(self, error):
        self.Mbox("Error", error, 0)
        sys.exit(1)        

"""Runs Functions from EPP files"""
class Functions():
    def __init__(self, manager):
        super().__init__()
        self.funcList = {'=':self.equal, 'var':self.Nvar}
        self.var = {"Null": None}
        self.manager = manager

    """Utility functions"""
    def useVars(self, perams):
        return str(tuple(perams[1:-1].split(",")))

    def setVar(self, varName, varValue):
        self.var[varName] = varValue

    def runFunc(self, line, i):
        if line[i] in self.funcList.keys():
            i = self.funcList[line[i]](line, i)
        else:
            self.manager.util.error(f'''Unknown Token on line: {" ".join(line)}''')

        return i

    """Functions to be run"""

    def equal(self, line, i):
        self.setVar(line[i-1], line[i+1])
        return i+2

    def Nvar(self, line, i):
        self.setVar(line[i + 1], None)
        return i+2


"""Holds a template"""
class Template():
    def __init__(self, manager):
        super().__init__()

def run():
    manager = Manager()

if __name__ == "__main__":
    run()
