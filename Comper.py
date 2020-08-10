"""This Compiles EPP files into configs"""

import ctypes
import sys
import pathlib
import re


class Manager:
    """Initialises other classes, and serves as a connector between them.
    Also holds general utility functions
    """

    def __init__(self):
        self.file_manager = FileManager()
        self.functions = Functions(self)

    def compile(self):
        self.files, self.templates = self.file_manager.read_files()

        for file in self.files:
            self.functions.execute(file[0], file[1])

    def message_box(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    def error(self, error):
        self.message_box("Error", error, 0)
        sys.exit(1)


class FileManager:
    """Loads/Writes to most of the EPP files"""
    def __init__(self):
        self.files = []
        self.path = pathlib.Path(__file__).parent.absolute()

    def write_override(self, text, filename):
        with open(self.path.parent / filename, "w") as f:
            f.write(text)

    def write(self, text, filename):
        with open(self.path.parent / filename, "a") as f:
            f.write(text)

    def read_files(self):
        self.files = list()
        self.templates = dict()

        for file in (self.path / "code").glob("*.epp"):
            with open(file) as f:
                self.files.append([file, self.parse_line(f.read())])

        for file in (self.path / "templates").glob("*.txt"):
            with open(file) as f:
                self.templates[file.stem] = Template(f.read())

        return self.files, self.templates

    def parse_line(self, txt):
        output = []
        txt = txt.replace("\n", "").split(";")
        for line in txt:
            output.append(line.split(" "))
        while [""] in output:
            output.remove([""])
        return output


class Functions:
    """Runs Functions from EPP files"""
    def __init__(self, manager):
        self.pos = 0
        self.epp_variables = {"Null": None}
        self.manager = manager
        self.write_value = None

        self.function_list = {
            "=": self.equal,
            "var": self.new_var,
            "template": self.new_template,
            "write": self.write
        }

# Utility functions

    def execute(self, path, file):
        self.path = path
        self.file = file

        for line in self.file:
            self.pos = 0
            while self.pos < len(line):
                self.run_function(line)

    def set_var(self, variable_name, variable_value):
        self.epp_variables[variable_name] = variable_value

    def run_function(self, line):
        if line[self.pos] in self.function_list.keys():
            self.function_list[line[self.pos]](line)
        else:
            self.manager.error(f"""Unknown Token on line: {" ".join(line)}""")

    def check_var(self, variable):
        if variable in self.epp_variables.keys():
            variable = self.epp_variables[variable]
        return variable

    def parse_parameters(self, parameters):
        return [self.check_var(parameter) for parameter in parameters.split(",")]

# Functions to be run

    def equal(self, line):
        self.set_var(line[self.pos - 1], line[self.pos + 1])
        self.pos += 2

    def new_var(self, line):
        self.set_var(line[self.pos + 1], None)
        self.pos += 2

    def new_template(self, line):
        if line[self.pos + 1].split("(")[0] in self.manager.templates.keys():
            template_name = line[self.pos + 1].split("(")
            self.set_var(template_name[0], self.manager.templates[template_name[0]])
            self.write_value = self.epp_variables[template_name[0]].var_output(self.parse_parameters(template_name[1][:-1]))

            print(self.write_value)

            self.pos += 2
        else:
            self.manager.error(
                f"""Unknown Template on line: {" ".join(line)}""")

    def write(self, line):
        self.manager.file_manager.write(self.write_value, self.path.stem + '.txt')


class Template:
    """Holds a template"""

    def __init__(self, txt):
        self.txt = txt

    def var_output(self, template_values):
        template_variables = re.findall(r"\[(.+?)\]", self.txt)

        if len(template_variables) != len(template_values):
            Manager().error(
                f"""Inproper Amount of Template Variables 
                Expected:{len(template_variables)}, Recived:{len(template_values)}"""
            )
        txt = self.txt

        for index, template_variable in enumerate(template_variables):
            txt = txt.replace(f"[{template_variable}]", template_values[index])

        return txt


def main():
    manager = Manager()
    manager.compile()


if __name__ == "__main__":
    main()
