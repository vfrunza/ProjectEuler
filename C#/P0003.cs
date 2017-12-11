using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Problem 0003 - Largest Prime Factor
//===============================================================================
//The prime factors 13195 are 5, 7, 13,and 29.

//What is the largest prime factor of 600851475143

//Answer: 6857
//===============================================================================

namespace ProjectEuler
{
    class P0003
    {
        public static Tuple<int, string> Problem()
        {
            long n = 600851475143;

            for (int i = Convert.ToInt32(Math.Sqrt(n)) + 1; i > 2; i -= 2)
            {
                //Console.WriteLine("Testing {0}", i);
                if (Utility.PrimeTest(i))
                {
                    if (n % i == 0)
                    {
                        return Tuple.Create(i, "3");
                    }
                }
            }
            return Tuple.Create(1, "3");
        }
    }
}
