using System.Reflection;
using System.Text.Json;
using Day2;

internal class Program
{
    private static async Task Main(string[] args)
    {
        var input = await GetFileContents();
        Console.WriteLine($"Day2, task1: {JsonSerializer.Serialize(Game.TotalScore(input))}");
        // Console.WriteLine($"Day1, task2: {JsonSerializer.Serialize(Puzzle.FindTopThree(input))}");
    }

    private static Task<string> GetFileContents()
    {
        var outPutDirectory = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
        return File.ReadAllTextAsync(Path.Combine(outPutDirectory, "lines.txt"));
    }
}
