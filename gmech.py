import math

class Gmech:
    """"""
    def __init__(self, weekly_pool=300000, matches_per_hour=3, points_per_game=10000, inactivity_time=5, inactivity_drop=0.20):
        """"""
        self.weekly_pool = weekly_pool
        self.matches_per_hour = matches_per_hour
        self.points_per_game = points_per_game
        self.inactivity_time = inactivity_time
        self.inactivity_drop = inactivity_drop

    def get_match_points(self, match_number):
        """"""
        #output = round(self.points_per_game * 1/pow(match_number+1,0.33))
        output = round(self.points_per_game * 1/(match_number+1))

        #Points never fall below 1000
        if output < 1000:
            output = 1000

        #print output
        return output