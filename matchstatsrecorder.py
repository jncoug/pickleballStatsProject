from data.rally import Rally
from data.error import Error
from data.winner import Winner
from typing import List


class MatchStatsRecorderInterface:
    def begin_match(self):
        pass


class MatchStatsRecorderDoubles(MatchStatsRecorderInterface):

    def __init__(self, match):
        self.match = match
        self.errorsT1P1 = None
        self.errorsT1P2 = None
        self.errorsT2P1 = None
        self.errorsT1P2 = None

        self.winnersT1P1 = None
        self.winnersT1P2 = None
        self.winnersT2P1 = None
        self.winnersT1P2 = None

    def begin_match(self):
            pass


class MatchStatsRecorderSingles(MatchStatsRecorderInterface):
    def __init__(self, match):
        self.match = match
        self.errorsP1 = None
        self.errorsP2 = None

        self.winnersP1 = None
        self.winnersP2 = None

    def begin_match(self):
        pass
