import gmech

class Merc:
    """"""
    def __init__(self, gmech, skill_level=1):
        """"""
        self.gmech = gmech

        self.this_weeks_pool = 0
        self.pool = 0
        self.points = 0

    def week(self, hours=0):
        """"""
        self.this_weeks_pool = self.gmech.weekly_pool

        # If the merc doesn't meet the minimum time, apply penalty on this_weeks_pool.
        if hours < self.gmech.inactivity_time:
            self.this_weeks_pool *= (1-self.gmech.inactivity_drop)

        # Week is over, add the remaining this_weeks_pool to pool
        self.pool = self.this_weeks_pool