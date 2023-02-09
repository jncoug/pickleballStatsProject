from dataclasses import dataclass


@dataclass
class Error:
    """Errors are defined as any shot that could have been reasonably made, but was missed for loss of the rally"""
    location: str  # baseline, transition, kitchen
    action: str  # volley, dink, drive, drop, atp, erne
    intent: str  # attack, reset, neutral
    shot: str  # fh, 1bh, 2bh
    game_number: int  # which game was this in the match (1-5)
    rally_number: int  # which rally was this in the game (1-999)

