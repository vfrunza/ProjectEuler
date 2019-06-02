using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    /// <summary>
    ///Problem 4 - Largest Palindrome Product.
    ///A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    ///Find the largest palindrome made from the product of two 3-digit numbers.
    ///Answer: 906609
    /// </summary>
    class Q0004
    {
        public static Tuple<int, string> OldProblem()
        {
            int Largest = 0;
            int CurrentInt;
            string Current;

            for (int x = 999; x >= 451; x -= 1)
            {
                for (int y = x; y >= 450; y -= 1)
                {
                    CurrentInt = x * y;
                    Current = CurrentInt.ToString();

                    if (Current[0] == Current[5] && Current[1] == Current[4] && Current[2] == Current[3])
                        if (CurrentInt > Largest)
                            Largest = CurrentInt;
                }
            }
            return Tuple.Create(Largest, "4");
        }

        public static Tuple<int, string> Problem()
        {
            string Current;
            int largest = 0;

            for (int x = 999; x >= 451; x -= 1)
                for (int y = x; y >= 450; y -= 1)
                {
                    if (x * y > largest)
                    {
                        Current = (x * y).ToString();
                        if (Current[0] == Current[5] && Current[1] == Current[4] && Current[2] == Current[3])
                            largest = x * y;
                    }
                }

            return Tuple.Create(largest, "4");
        }
    }
}
