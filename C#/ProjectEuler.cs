using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using RecordingUtility;
using ProblemUtility;
using System.Diagnostics;

namespace ProjectEuler
{
    class ProjectEuler
    {
        static void Main(string[] args)
        {
            int loops = 1;
            int counter = 0;
            Tuple<int, string> result = Tuple.Create(0, "");

            Stopwatch watch = new Stopwatch();
            watch.Start();

            while (counter != loops)
            {
                result = Q0007.Problem();
                counter++;
            }
            watch.Stop();
            double time = Convert.ToDouble(watch.ElapsedMilliseconds) / (loops * 1000.0);

            Console.WriteLine("{0} | {1}", DataFormatting.ToEngineeringNotation(time, "s"), result.Item1);
            DataFormatting.SaveResults(result.Item2, DataFormatting.ToEngineeringNotation(time, "s"));

            Pause();
        }

        public static void Pause()
        {
            Console.WriteLine("\nPress any key to exit...");
            Console.ReadKey();
        }
    }
}
