from dataclasses import dataclass


@dataclass
class Rally:
    rally_winner: int  # which team won the rally (1-2)
    rally_loser: int  # which team lost the rally (1-2)
    causal_player: str  # which team/player caused the rally to end (1 or 2)
    game_number: int  # which game was this in the match (1-5)
    rally_number: int  # which rally was this in the game (1-999)
