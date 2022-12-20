using System.Linq;
using System.Numerics;

namespace Day1.Lib;

public class Puzzle
{
    public static Result FindHeaviestElf(string input)
    {
        var rows = input.Trim().Split("\n");
        var groups = CollectGroups(rows);
        var max = groups.MaxBy((g) => g.Sum());

        return new Result {
            Total = max!.Sum(),
            Position = groups.FindIndex((g) => g == max)
        };
    }

    private static List<ElfGroup> CollectGroups(string[] rows)
    {
        var groups = new List<ElfGroup>
        {
            new ElfGroup()
        };
        foreach (string row in rows) {
            if (Int32.TryParse(row, out int number)) {
                groups.Last<ElfGroup>().Members.Add(number);
            } else {
                groups.Add(new ElfGroup());
            }
        }
        return groups;
    }

    public static ListResult FindTopThree(string input)
    {
        var rows = input.Trim().Split("\n");
        var groups = CollectGroups(rows);
        var sorted = groups
            .Select((g, i) => new {Index = i, Total = g.Sum()})
            .OrderBy((g) => -g.Total).Take(3).ToList();


        return new ListResult
        {
            Total = sorted.Sum((g) => g.Total),
            List = sorted.Select((g) =>
                new Result()
                {
                    Position = g.Index,
                    Total = g.Total
                }
            ).ToList()
        };
    }
}

internal class ElfGroup
{
    public List<int> Members { get;set; } = new List<int>();

    public int Sum() {
        return Members.Sum();
    }
}
