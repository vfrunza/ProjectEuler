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
            List<int> MultipuleList = new List<int>();
            //{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};

            MultipuleList.AddRange(Enumerable.Range(30,33));


            return MultipuleList.Aggregate((x, y) => Utility.LCM(x, y));
        }
    }
}
