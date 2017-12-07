#MAIN
#===============================================================================
#Replacing the noted function inside main will run that particular problem.
#===============================================================================

from timeit import default_timer as timer
import subprocess
import os
from p0006 import problem

def main():
    loops = 10

    start = timer()
    for x in range (0, loops):
        result, problem_name = problem()
    end = timer()

    print(str((end - start) / loops) + " seconds | " + str(result))

    command = 'cd ..; python3 ResultUpdater.py 1 ' + problem_name + ' ' + str((end - start) / loops)
    subprocess.call(command, shell=True)

main()