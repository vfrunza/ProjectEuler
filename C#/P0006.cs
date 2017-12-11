using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class P0006
    {
        public static Tuple<int, string> Problem()
        {
            int limit = 100;

            return Tuple.Create(Utility.SquareOfSum(limit) - Utility.SumOfSquares(limit), "6");
        }
    }
}
