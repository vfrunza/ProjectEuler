using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ProblemUtility;

namespace ProjectEuler
{
    /// <summary>
    ///Problem 7 - 10001st prime.
    ///By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    ///What is the 10 001st prime number?
    ///Answer: 
    /// </summary>
    class Q0007
    {
        public static Tuple<int, string> Problem()
        {
            int count = 0;
            int i = 1;

            while (count != 10001)
            {
                i++;
                if (Prime.isPrime(i))
                    count++;
            }
            return new Tuple<int, string>(i, "7");
        }
    }
}
