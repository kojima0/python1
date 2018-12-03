class Basaball_Team:
    def __init__(self,name,win,lose,draw):
        self.name = name
        self.win = win
        self.lose = lose
        self.draw = draw

    def calc_win_rate(self):
            x = 0.0
            x = float(self.win / (self.win + self.lose))
            return(round(x,3))

    def show_team_result(self):
        # print(self.name,self.win,self.lose,self.draw,self.calc_win_rate())
        print(f"{self.name:8s} {self.win:3d}  {self.lose:3d}  {self.draw:3d} {self.calc_win_rate():.3f}")

    @classmethod
    def description(self):
        print("team win lose draw rate")
