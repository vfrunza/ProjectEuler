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

        public static List<int> Factorize(int n)
        {
            List<int> Factors = new List<int>();

            for (int i = n - 1; i > 0; i--)
            {
                if (n % i == 0)
                {
                    if (!Factors.Contains(i))
                    {
                        Factors.Add(i);
                    }
                }
            }
            return Factors;
        }

        public static int GCD(int a, int b)
        {
            if (b == 0)
            {
                return a;
            }
            else
            {
                return GCD(b, a % b);
            }
        }

        public static int LCM(int a, int b)
        {
            return (a * b) / GCD(a, b);
        }
    }
}
