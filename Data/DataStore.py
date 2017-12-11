# Will analyse the results files of each langauge folder and compile it into one master copy and will produce an updated README.

import EngNotation
from tabulate import tabulate

def main():
    results = EulerData()

    results = get_problems(results)

    #open C/C++
    #results = combine_data(results, "C/C++")
    results = combine_data(results, "Python")
    results = combine_data(results, "CSharp")

    print(results)

    compile_readme(results)

def update_master(results):
    pass

def compile_readme(results):
    readme = open("../README.md", "w")
    introduction = "# ProjectEuler\nMy solutions to problems on Project Euler as I finish them. You can learn more about Project Euler here, https://projecteuler.net/about.\nAll of the solutions are timed, with the time of the original version I wrote (usually a very basic brute force approach) and the timings for the most up to date version. Usually I will only include the final version of the problem in my code, but it is all visible on git. If a former solution is particularly interesting, I may decide to leave it in the code, renaming the function to problem1().\nBelow is the execution time for each problem in milliseconds. Timer is used in python and stopwatch is used in C#. each program is run in at least 100 loops, and then the time is divided by the number of loops to get the time of one instance.\nC# is run with the Visual Studio Microsoft Compiler and Python is run in WSL bash using python3.\n\n# Results\n\n"
    readme.write(introduction)
    readme.write("| Title | C | C++ | C# | D | Java | JavaScript | Python 3 | Rust | R |\n")
    readme.write("| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n")

    first_line = True
    for line in results.data:
        if first_line:
            first_line = False
        else:
            readme.write("| " + str(line[0]) + ". " + str(line[1]) + " | " + str(line[2]) + " | " + str(line[3]) + " | " + str(line[4]) + " | " + str(line[5]) + " | " + str(line[6]) + " | " + str(line[7]) + " | " + str(line[8]) + " | " + str(line[9]) + " | " + str(line[10]) + " |\n")

def get_problems(results):
    problems = open("problems.csv", "r").readlines()

    for line in problems:
        line = line.strip("\n").split(",")
        results.data.append([int(line[0]), line[1], " ", " ", " ", " ", " ", " ", " ", " ", " "])
    
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
                    line[8] = pyline[1]
                    break
        py_file.close() 
    
    if lang == "CSharp":
        c_file = open("../C#/bin/Release/results.csv", "r+")
        c_data = c_file.readlines()

        for cline in c_data:
            cline = cline.strip("\n").split(",")
            for line in results.data:
                if line[0] == int(cline[0]):
                    line[4] = cline[1]
                    break
        c_file.close() 

    return results

class EulerData:

    def __init__(self):
        self.data = [["Number","Title", "C", "C++", "C#", "D", "Java", "JavaScript", "Python", "Rust", "R"]]

    def __str__(self):
        return "\n" + tabulate(self.data[1:], self.data[0])

main()