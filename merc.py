import gmech

class Merc:
    """"""
    def __init__(self, gmech, skill_level=1):
        """"""
        self.gmech = gmech

        self.this_weeks_pool = 0
        self.pool = 0
        self.points = 0
        self.week = 0

        self.assumed_weekly_hours = 0

    def play(self, hours=0):
        """"""
        self.this_weeks_pool = self.gmech.weekly_pool

        # Add skill points for each match.
        for i in range(hours*self.gmech.matches_per_hour):
            self.points += self.gmech.get_match_points(0, i)
            self.this_weeks_pool -= self.gmech.get_match_points(self.week, i)

        # If the merc doesn't meet the minimum time, apply penalty on this_weeks_pool.
        if hours < self.gmech.inactivity_time:
            self.this_weeks_pool *= (1-self.gmech.inactivity_drop)

        # Week is over, add the remaining this_weeks_pool to pool
        self.pool += self.this_weeks_pool
        self._update_weekly_hours(hours)

    def _update_weekly_hours(self, hours):
        """"""
        self.assumed_weekly_hours = (self.assumed_weekly_hours*self.week + hours)/(self.week+1)
        self.week += 1
