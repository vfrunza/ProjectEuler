using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Problem 0001 - Multiples of 3 and 5
//===============================================================================
//If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

//Find the sum of all the multiples of 3 or 5 below 1000.

//Answer: 233168
//Time: 0.8832 Seconds Per 10,000 iterations
//===============================================================================

namespace ProjectEuler
{
    class P0001
    {
        public static int Problem()
        {
            int counter = 1;
            int M3, M5;
            HashSet<int> Multipules = new HashSet<int>();

            while (true)
            {
                M3 = 3 * counter;
                M5 = 5 * counter;

                if (M3 >= 1000 && M5 >= 1000)
                {
                    break;
                }

                if (M3 == M5)
                {
                    Multipules.Add(M3);
                }
                else
                {
                    Multipules.Add(M3);

                    if (M5 < 1000)
                    {
                        Multipules.Add(M5);
                    }
                }

                counter += 1;

            }
            return Multipules.Sum();
        }
    }
}
