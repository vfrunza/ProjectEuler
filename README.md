# ProjectEuler

My solutions to problems on Project Euler as I finish them. You can learn more about Project Euler here, https://projecteuler.net/about.

All of the solutions are timed, with the time of the original version I wrote (usually a very basic brute force approach) and the timings for the most up to date version. Usually I will only include the final version of the problem in my code, but it is all visible on git. If a former solution is particularly interesting, I may decide to leave it in the code, renaming the function to problem1().

All of the programs have the same structure, with timings given by timeit

    # Problem 0xxx - Title
    #===============================================================
    # The problem statment from Project Euler

    # Answer: 
    # First Version Time: xx.xxxx Seconds Per xxx iterations
    # Second Version Time: xx.xxxx Seconds Per xxx iterations
    #===============================================================

    from timeit import default_timer as timer

    def main():
        loops = 1

        start = timer()
        for x in range (0, loops):

            result = problem()

        end = timer()

        print(result)
        print(str((end - start)) + " seconds") 

    def problem():

    main()