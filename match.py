class Match:

    def __init__(self, team_1, team_2, games_to_play, points_to_play, rally=False):

        self.team_1 = team_1
        # team 1 player 1, etc
        self.t1p1 = None
        self.t1p2 = None
        self.team_2 = team_2
        self.t2p1 = None
        self.t2p2 = None
        self.games_to_play = games_to_play
        self.points_to_play = points_to_play
        self.rally = rally

        self.scoring = "rally" if self.rally else "traditional"

        # split the teams into separate players
        self.singles = None
        self.split_teams()

    def __str__(self):
        if self.singles:

            return "Singles Match:\n%s vs %s\n" \
                   "Format: %s game(s) to %s, %s scoring." \
                % (self.team_1, self.team_2, self.games_to_play, self.points_to_play, self.scoring)
        else:
            return "Doubles Match:\n%s and %s vs %s and %s\n" \
                   "Format: %s game(s) to %s, %s scoring." \
                % (self.t1p1, self.t1p2, self.t2p1, self.t2p2, self.games_to_play, self.points_to_play, self.scoring)

    def split_teams(self):
        team_1_split = self.team_1.split(", ")
        try:
            self.t1p1 = team_1_split[0]
            self.t1p2 = team_1_split[1]

            team_2_split = self.team_2.split(", ")
            self.t2p1 = team_2_split[0]
            self.t2p2 = team_2_split[1]

            self.singles = False

        except IndexError:
            self.singles = True

