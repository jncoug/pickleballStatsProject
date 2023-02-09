from match import *
from matchstatsrecorder import *


def setup_match():
    print("***********************")
    print("If a doubles match, please separate the team's players with a comma and a space. (i.e 'Ben Johns, Anna Leigh"
          " Waters',"
          "or 'JW Johnson, Dylan Frazier')")
    print("***********************")
    team_1 = input("Team 1 player(s): ")
    team_2 = input("Team 2 player(s): ")
    games = input("Best of how many games (i.e. 3): ")
    points = input("Points per game (i.e. 11): ")
    rally = input("Rally scoring? (y/n): ")
    rally_answer = True if rally == "y" else False

    return Match(team_1, team_2, games, points, rally_answer)


if __name__ == '__main__':
    match = setup_match()
    print(match)

    if not match.singles:
        recorder = MatchStatsRecorderDoubles(match)
    else:
        recorder = MatchStatsRecorderSingles(match)

    # start the code to record the match stats
    recorder.begin_match()


