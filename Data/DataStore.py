# Will analyse the results files of each langauge folder and compile it into one master copy and will produce an updated README.

import EngNotation
from tabulate import tabulate

def main():
    results = EulerData()

    results = get_problems(results)

    #open C/C++
    results = combine_data(results, "C/C++")
    results = combine_data(results, "Python")

    print(results)

def update_master(results):
    pass

def compile_readme(results):
    pass

def get_problems(results):
    problems = open("problems.csv", "r").readlines()

    for line in problems:
        line = line.strip("\n").split(",")
        results.data.append([int(line[0]), line[1], " ", " ", " ", " ", " ", " ", " ", " "])
    
    return results

def combine_data(results, lang):
    if lang == "C/C++":
        c_file = open("../C++/results.csv", "r+")
        c_data = c_file.readlines()

        for cline in c_data:
            cline = cline.strip("\n").split(",")
            for line in results.data:
                if line[0] == int(cline[0]):
                    line[2] = cline[1]
                    break
        c_file.close() 

    if lang == "Python":
        py_file = open("../Python/results.csv", "r+")
        py_data = py_file.readlines()

        for pyline in py_data:
            pyline = pyline.strip("\n").split(",")
            for line in results.data:
                if line[0] == int(pyline[0]):
                    line[7] = pyline[1]
                    break
        py_file.close() 
    return results

class EulerData:

    def __init__(self):
        self.data = [["Problem Number","Problem Title", "C", "C++", "C#", "D", "Java", "Python", "Rust", "R"]]

    def __str__(self):
        return "\n" + tabulate(self.data[1:], self.data[0])

main()