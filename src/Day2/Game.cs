namespace Day2;

public class Game
{
    public static Result TotalScore(string input)
    {
        var rows = input.Trim().Split("\n");
        var scores = rows.Select((row) => {
            var moves = row.Split(" ").Select(ToolMap.Parse).ToArray();
            return ToolMap.ScoreMove(moves[0], moves[1]);
        }).ToList();

        return new Result
        {
            Total = scores.Sum(),
            Rounds = scores
        };
    }
}
