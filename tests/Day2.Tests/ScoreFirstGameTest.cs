using System.Text.Json;
using FluentAssertions;

namespace Day2.Tests;

public class ScoreFirstGameTest
{
    [Fact]
    public void TestScoringOfGame()
    {
        var input = "A Y\nB X\nC Z";
        var result = Game.TotalScore(input);
        result.Total.Should().Be(15, JsonSerializer.Serialize(result));
        result.Rounds.Should().BeEquivalentTo(new List<int> { 8, 1, 6 }, JsonSerializer.Serialize(result));
    }
}
