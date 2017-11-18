using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UtilityLibrary;

namespace ProjectEuler
{
    class Program
    {
        static void Main(string[] args)
        {
            int loops = 100000;
            int result = 0;

            System.Diagnostics.Stopwatch watch = System.Diagnostics.Stopwatch.StartNew();
            while (loops != 1)
            {
                result = P0001.Problem();
                loops--;
            }
            watch.Stop();
            double elapsedMs = Convert.ToDouble(watch.ElapsedMilliseconds) / (1000.0);

            Console.WriteLine("{0} seconds | {1}", elapsedMs, result);

            //UtilityLibrary.Utility.Pause();
        }
    }
}
