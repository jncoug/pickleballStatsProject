from dataclasses import dataclass


@dataclass
class Speedup:
    """Speedups are defined as an aggressive shot made during a neutral rally or position"""
    location: str  # almost always the kitchen, sometimes transition zone
    action: str  # volley, bounce
    shot: str  # fh, 1bh, 2bh
    game_number: int  # which game was this in the match (1-5)
    rally_number: int  # which rally was this in the game (1-999)
