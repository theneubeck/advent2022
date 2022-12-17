using Xunit;
using FluentAssertions;
using day1.lib;

namespace day1.tests;

public class FindHeaviestTest
{
    [Fact]
    public void TestFindHeaviestElf()
    {
        var input = @"
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";
        var result = Puzzle.FindHeaviestElf(input);
        result.Total.Should().Be(24000);
        result.Position.Should().Be(3);
    }
}
