import ctypes
import sys
import os
from ast import literal_eval
import pathlib
"""This Compiles EPP files into configs"""

class Manager():
    """Initialises other classes, and serves as a connector between them.
    Also holds general utility functions"""

    def __init__(self):
        super().__init__()
        self.FileM = FileManager(self)
        self.Func = Functions(self)

    def Compile(self):
        self.files = self.FileM.readFiles()
        self.FileM.clearOutputFiles()
        self.Func.execute(self.FileM.files.pop(0))

    def Mbox(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    def error(self, error):
        self.Mbox("Error", error, 0)
        sys.exit(1)


class FileManager():
    """Loads/Writes to most of the EPP files"""

    def __init__(self, manager):
        super().__init__()
        self.files = []
        self.manager = manager
        self.path = pathlib.Path(__file__).parent.absolute()

    def write(self, lines):
        with open(str(self.path.parent.parent) + "\creatures.txt", "a") as f:
            f.write(lines)

    def clearOutputFiles(self):
        with open(str(self.path.parent.parent) + "\creatures.txt", "w") as f:
            f.write("")

    def readFiles(self):
        self.files = []

        with open(str(self.path.parent) + "\code\Epp_creatures.txt") as f:
            self.files.append(self.parseLine(f.read()))

        return self.files

    def parseLine(self, txt):
        output = []
        txt = txt.replace("\n", "").split(";")

        for line in txt:
            output.append(line.split(" "))

        while ([""] in output):
            output.remove([""])

        return output


class Functions():
    """Runs Functions from EPP files"""

    def __init__(self, manager):
        super().__init__()
        self.pos = 0
        self.funcList = {'=': self.equal, 'var': self.Nvar}
        self.var = {"Null": None}
        self.manager = manager

#   ###Utility functions###

    def execute(self, file):
        for line in file:
            self.pos = 0
            while self.pos < len(line):
                self.runFunc(line)

    def useVars(self, perams):
        return str(tuple(perams[1:-1].split(",")))

    def setVar(self, varName, varValue):
        self.var[varName] = varValue

    def runFunc(self, line):
        if line[self.pos] in self.funcList.keys():
            self.funcList[line[self.pos]](line)
        else:
            self.manager.error(f'''Unknown Token on line: {" ".join(line)}''')


#   ###Functions to be run###

    def equal(self, line):
    
        self.setVar(line[self.pos - 1], line[self.pos + 1])
        self.pos += 2

    def Nvar(self, line):
        self.setVar(line[self.pos + 1], None)
        self.pos += 2


class Template():
    """Holds a template"""

    def __init__(self, ):
        super().__init__()




def run():
    manager = Manager()
    manager.Compile()


if __name__ == "__main__":
    run()
