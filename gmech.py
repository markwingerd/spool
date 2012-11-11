import math

class Gmech:
    """"""
    def __init__(self, weekly_pool=300000, matches_per_hour=3, points_per_game=5000, inactivity_time=5, inactivity_drop=0.20):
        """"""
        self.weekly_pool = weekly_pool
        self.matches_per_hour = matches_per_hour
        self.points_per_game = points_per_game
        self.inactivity_time = inactivity_time
        self.inactivity_drop = inactivity_drop

    def get_match_points(self, week_number, match_number):
        """"""
        output = 0
        # The first week is a sample period.
        if week_number is 0:
            multiplier = float(100-match_number)/100
            if multiplier < 0:
                multiplier = 0
            output = (self.points_per_game-1000)*multiplier +1000

        return output