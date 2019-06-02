using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProblemUtility
{
    public static class Prime
    {
        /// <summary>
        /// Tests to see if the given integer is a prime number
        /// </summary>
        /// <param name="n">Potential prime number to test</param>
        /// <returns></returns>
        public static bool isPrime(int n)
        {
            if (n <= 3)
            {
                return n >= 2;
            }
            if (n % 2 == 0 || n % 3 == 0)
            {
                return false;
            }
            for (int i = 5; i <= Convert.ToInt32(Math.Sqrt(n)) + 1; i += 6)
            {
                if (n % i == 0 || n % (i + 2) == 0)
                {
                    return false;
                }
            }
            return true;
        }
    }
}
