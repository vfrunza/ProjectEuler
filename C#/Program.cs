using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class Program
    {
        static void Main(string[] args)
        {
            int loops = 100;
            int counter = 0;
            Tuple<int, string> result = Tuple.Create(0, "");

            System.Diagnostics.Stopwatch watch = new System.Diagnostics.Stopwatch();
            watch.Start();
            while (counter != loops)
            {
                result = P0006.Problem();
                counter++;
            }
            watch.Stop();
            double time = Convert.ToDouble(watch.ElapsedMilliseconds) / (loops * 1000.0);

            Console.WriteLine("{0} | {1}", ToEngineering(time, "s"), result.Item1);
            SaveResults(result.Item2, ToEngineering(time, "s"));

            Utility.Pause();
        }
        public static string ToEngineering(double value, string unitName)
        {
            int exp = (int)(Math.Floor(Math.Log10(value) / 3.0) * 3.0);
            double newValue = value * Math.Pow(10.0, -exp);
            if (newValue >= 1000.0)
            {
                newValue = newValue / 1000.0;
                exp = exp + 3;
            }
            var symbol = String.Empty;
            switch (exp)
            {
                case 3:
                    symbol = "k";
                    break;
                case 6:
                    symbol = "M";
                    break;
                case 9:
                    symbol = "G";
                    break;
                case 12:
                    symbol = "T";
                    break;
                case -3:
                    symbol = "m";
                    break;
                case -6:
                    symbol = "μ";
                    break;
                case -9:
                    symbol = "n";
                    break;
                case -12:
                    symbol = "p";
                    break;
            }
            return string.Format("{0:##0.0} {1}{2}", newValue, symbol, unitName);
        }

        public static void SaveResults(string problem, string time)
        {
            string[] lines = File.ReadAllLines("results.csv");
            List<List<string>> results = new List<List<string>>();
            string resultsString = "";
            bool updated = false;

            foreach (string line in lines)
            {
                results.Add(line.Replace("\n", String.Empty).Split(',').ToList<string>());
            }

            foreach (List<string> line in results)
            {
                if (line[0] == problem)
                {
                    line[1] = time;
                    updated = true;
                    break;
                }
            }

            if (!updated)
            {
                List<string> append = new List<string>() { problem, time };
                results.Add(append);
            }

            foreach(List<string> line in results)
            {
                resultsString = resultsString + line[0] + "," + line[1] + "\n";
            }
            File.WriteAllText("results.csv", resultsString);
        }
    }
}
