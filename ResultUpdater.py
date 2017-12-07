import sys
from EngNotation import eng_notate

language = sys.argv[1]
problem = sys.argv[2]
time = sys.argv[3] #time in milliseconds

Results = []
Instructions = """# ProjectEuler\n\nMy solutions to problems on Project Euler as I finish them. You can learn more about Project Euler here, https://projecteuler.net/about.\n\nAll of the solutions are timed, with the time of the original version I wrote (usually a very basic brute force approach) and the timings for the most up to date version. Usually I will only include the final version of the problem in my code, but it is all visible on git. If a former solution is particularly interesting, I may decide to leave it in the code, renaming the function to problem1().\n\nBelow is the execution time for each problem in milliseconds. Timer is used in python and stopwatch is used in C#. each program is run in at least 100 loops, and then the time is divided by the number of loops to get the time of one instance.\n\nC# is run with the Visual Studio Microsoft Compiler and Python is run in WSL bash using python3.\n\n| Problem | Python | C# | C++ | Rust |\n"""

File = open("Results.csv", "r+")
ResultsFile = File.readlines()

ReadFile = open("README.md", "w")

for line in ResultsFile:
    Results.append(line.strip("\n").split(","))

found = False
for row in range(0, len(Results)):
    if Results[row][0] == problem:
        Results[row][int(language)] = eng_notate(float(time)) + "s"
        found = True
        
if found == False:
    if language == "1":
        Results.append([problem, eng_notate(float(time)) + "s", "", "", ""])


File.seek(0)
File.truncate()

for row in Results:
    File.write(",".join(row) + "\n")

ReadFile.write(Instructions) 

for row in Results:
    ReadFile.write("| " + " | ".join(row) + " |\n")





