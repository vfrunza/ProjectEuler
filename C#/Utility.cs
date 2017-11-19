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
