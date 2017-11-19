using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class Utility
    {
        public static bool PrimeTest(int n)
        {
            double MAXSearch = Math.Sqrt(n) + 1;
            int counter = 5;
            if (n <= 3)
            {
                return n >= 2;
            }
            if (n % 2 == 0 || n % 3 == 0)
            {
                return false;
            }
            while (counter < MAXSearch)
            {
                if (n % counter == 0 || n % (counter + 2) == 0)
                {
                    return false;
                }
            }
            return true;
        }
    }
}
