#MAIN
#===============================================================================
#Replacing the noted function inside main will run that particular problem.
#===============================================================================

from timeit import default_timer as timer
from Utility import save
from EngNotation import eng_notate

from p0006 import problem

def main():
    loops = 100

    start = timer()
    for x in range (0, loops):
        result, problem_num = problem()
    end = timer()

    time = eng_notate(float(end - start) / loops) + "s"
    print(time + " | " + str(result))

    save(problem_num, time)

main()