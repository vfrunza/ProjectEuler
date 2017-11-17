#MAIN
#===============================================================================
#Replacing the noted function inside main will run that particular problem.
#===============================================================================

from timeit import default_timer as timer
from p0004 import problem

def main():
    loops = 10

    start = timer()
    for x in range (0, loops):
        result = problem()
    end = timer()

    print(str((end - start)) + " seconds | " + str(result)) 

main()