﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Problem 0003 - Largest Prime Factor
//===============================================================================
//The prime factors 13195 are 5, 7, 13,and 29.

//What is the largest prime factor of 600851475143

//Answer: 6857
//Time: 131.0388 Seconds Per 100 iterations
//===============================================================================

namespace ProjectEuler
{
    class P0003
    {
        public static int Problem()
        {
            long n = 600851475143;

            for (int i = Convert.ToInt32(Math.Sqrt(n)) - 1; i > 2; i -= 2)
            {
                if (Utility.PrimeTest(i))
                {
                    if (n % i == 0)
                    {
                        return i;
                    }
                }
            }
            return 1;
        }
    }
}