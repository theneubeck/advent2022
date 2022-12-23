namespace Day2;

class ToolMap
{
    private static readonly Dictionary<string, Tool> Map = new()
    {
        {"A", Tool.Rock},
        {"B", Tool.Paper},
        {"C", Tool.Scissors},
        {"Y", Tool.Paper},
        {"X", Tool.Rock},
        {"Z", Tool.Scissors},
    };

    private static readonly Dictionary<Tool, Tool> WinMap = new()
    {
        {Tool.Rock, Tool.Paper},
        {Tool.Paper, Tool.Scissors},
        {Tool.Scissors, Tool.Rock}
    };

    public static Tool Parse(string symbol)
    {
        return Map[symbol];
    }

    public static int ScoreMove(Tool they, Tool you)
    {
        var score = (int) you;
        if (they == you) {
            score += (int)GameResult.Draw;
        } else if (WinMap[they] == you) {
            score += (int) GameResult.Win;
        }

        return score;
    }
}
