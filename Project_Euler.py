#MAIN
#===============================================================================
#Replacing the noted function inside main will run that particular problem.
#===============================================================================

from timeit import default_timer as timer
from p0007 import problem

def main():
    loops = 1000

    start = timer()
    for x in range (0, loops):
        result = problem()
    end = timer()

    print(str((end - start)) + " seconds | " + str(result)) 

main()