using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class P0006
    {
        public static int Problem()
        {
            int limit = 100;

            return Utility.SquareOfSum(limit) - Utility.SumOfSquares(limit);
        }
    }
}
