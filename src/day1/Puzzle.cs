using System.Linq;
using System.Numerics;

namespace day1.lib;

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
}

internal class ElfGroup
{
    public List<int> Members { get;set; } = new List<int>();

    public int Sum() {
        return Members.Sum();
    }
}
