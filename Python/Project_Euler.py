#MAIN
#===============================================================================
#Replacing the noted function inside main will run that particular problem.
#===============================================================================

from timeit import default_timer as timer
from p0004 import problem

def main():
    loops = 100

    start = timer()
    for x in range (0, loops):
        result = problem()
    end = timer()

    print(str((end - start) * 1000 / loops) + " milliseconds | " + str(result))

main()