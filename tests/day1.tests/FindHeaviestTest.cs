using Xunit;
using FluentAssertions;
using Day1.Lib;

namespace Day1.Tests;

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

    [Fact]
    public void TestFindTopThree()
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
        var result = Puzzle.FindTopThree(input);
        result.Total.Should().Be(45000);
        result.List.Should().BeEquivalentTo(new List<Result>
        {
            new() {Total = 24000, Position = 3},
            new() {Total = 11000, Position = 2},
            new() {Total = 10000, Position = 4}
        });
    }
}
