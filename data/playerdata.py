from dataclasses import dataclass
from error import Error
from winner import Winner
from speedup import Speedup
from typing import List


@dataclass
class PlayerData:
    name: str
    errors: List[Error]
    winners: List[Winner]
    speedups: List[Speedup]
