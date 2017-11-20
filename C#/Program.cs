using System;
using System.Collections.Generic;
using System.Diagnostics;
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
            int loops = 1;
            int counter = 0;
            int result = 0;

            System.Diagnostics.Stopwatch watch = System.Diagnostics.Stopwatch.StartNew();
            while (counter != loops)
            {
                result = P0005.Problem();
                counter++;
            }
            watch.Stop();
            double elapsedMs = Convert.ToDouble(watch.ElapsedMilliseconds) / Convert.ToDouble(loops);

            Console.WriteLine("{0} milliseconds | {1}", elapsedMs, result);

            UtilityLibrary.Utility.Pause();
        }
    }
}
