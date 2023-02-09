from dataclasses import dataclass


@dataclass
class Winner:
    """Winners are defined as an attacking or aggressive shot that directly wins the rally"""
    location: str  # baseline, transition, kitchen
    action: str  # overhead, volley, dink, drive, drop, atp, erne
    intent: str  # attack, reset, neutral
    shot: str  # fh, 1bh, 2bh
    game_number: int  # which game was this in the match (1-5)
    rally_number: int  # which rally was this in the game (1-999)
