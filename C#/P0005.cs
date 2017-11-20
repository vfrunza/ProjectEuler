using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//#Problem 0005 - Smallest Multiple
//===============================================================================
//2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

//What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

//Answer: 232792560
//===============================================================================
namespace ProjectEuler
{
    class P0005
    {
        public static int Problem()
        {
            return Utility.LCM(Utility.LCM(Utility.LCM(Utility.LCM(Utility.LCM(Utility.LCM(Utility.LCM(Utility.LCM(Utility.LCM(20, 19), 18), 17), 16), 15), 14), 13), 12), 11);
        }
    }
}
