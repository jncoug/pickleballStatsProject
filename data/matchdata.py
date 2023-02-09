from dataclasses import dataclass
from rally import Rally
from playerdata import PlayerData
from typing import List


@dataclass
class MatchData:
    team1: List[PlayerData]  # each player on team 1
    team2: List[PlayerData]  # each player on team 2
    rallies: List[Rally]  # a list of all rallies and the result
    winning_team: int  # which team won the match (1 or 2)
    winning_score: int  # how many points did this team get
    losing_score: int  # how many points did this team get
