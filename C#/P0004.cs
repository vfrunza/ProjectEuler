using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Problem 0004 - Largest Palindrome Product
//===============================================================================
//A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

//Find the largest palindrome made from the product of two 3-digit numbers.

//Answer: 906609
//===============================================================================

namespace ProjectEuler
{
    class P0004
    {
        public static Tuple<int, string> Problem()
        {
            int Largest = 0;
            int CurrentInt;
            string Current;

            for (int x = 999; x >= 450; x -= 1)
            {
                for (int y = x; y >= 450; y -= 1)
                {
                    CurrentInt = x * y;
                    Current = Convert.ToString(CurrentInt);

                    if (CurrentInt > Largest)
                    {
                        if (Current.Length == 5)
                        {
                            if (Current[0] == Current[4] && Current[1] == Current[3])
                            {
                                if (CurrentInt > Largest)
                                {
                                    Largest = CurrentInt;
                                }
                            }
                        }
                        else
                        {
                            if (Current[0] == Current[5] && Current[1] == Current[4] && Current[2] == Current[3])
                            {
                                if (CurrentInt > Largest)
                                {
                                    Largest = CurrentInt;
                                }
                            }
                        }
                    }
                }
            }
            return Tuple.Create(Largest, "4");
        }
    }
}
