import math

class Gmech:
    """"""
    def __init__(self, weekly_pool=500000, matches_per_hour=3,
                 inactivity_time=10, inactivity_drop=0.40, weeks_in_history=3, 
                 points_min=1000, default_matches=100):
        """Init for all Gmech variables."""
        self.weekly_pool = weekly_pool
        self.matches_per_hour = matches_per_hour
        self.inactivity_time = inactivity_time
        self.inactivity_drop = inactivity_drop
        self.weeks_in_history = weeks_in_history
        self.points_min = points_min
        self.default_matches = default_matches
        # Used when a merc does not exceed the inactivity time.
        self.max_points_per_match = weekly_pool / (inactivity_time*matches_per_hour)

    def get_point_reduction(self, hours, this_weeks_pool):
        """Returns points that will be subtracted from a weekly pool."""
        # Step out if this weeks pool is negative.
        if this_weeks_pool < 0:
            return 0
        # If a merc doesn't meet inactivity time, apply reduction to remaining pool.
        if hours < self.inactivity_time:
            slope = -1 * self.inactivity_drop / self.inactivity_time
            penalty = slope * hours + self.inactivity_drop
            return round(this_weeks_pool * penalty)
        else: 
            return 0

    def get_match_points_no_history(self, match_number, pool):
        """Returns the points based on the match_number if no history has
        been established."""
        # Establish Equation
        points_max = round(pool/self.default_matches)
        slope = -1 * ((points_max-self.points_min)/self.default_matches)
        output = round((slope * match_number) + points_max)
        # Slope should not be positive. Returning min_points is sufficent.
        # If output is too low, return the minimum points gained.
        if (slope > 0) or (output < self.points_min):
            return self.points_min
        return output

    def get_match_points(self, match_number, history, pool):
        """Returns the points for the match_number.
        This method has 3 phases and an equation for each phase. Phase 1 is
        when match_number is less then the assumed_matches value and it returns
        a flat portion of pool. In this phase, the points degrade very slowly
        at about 30 percent over the entire phase. Phase two is active any time
        match_number is equal or over assumed_matches and the output degrades
        very sharply. Phase 3 is active anytime the output falls below the 
        point_min value.  Finally this method will catch potential errors like
        the output being too high or the output exceeding the given pool and will
        return the output."""
        # Establish initial values.
        slope_modifier=0.9      # Controls the degrade of SP over time. This is primarily used for the first phase of this function so the pool isn't completely consumed.
        assumed_matches = history * self.matches_per_hour
        # If match is under assumed_matches, output is in first phase (plateaued).
        # If match is equal or over, output is in second phase (degrading).
        # If output is ever below points_min, return third phased value (base).
        if match_number < assumed_matches:
            output = round(pool / (assumed_matches-(match_number*slope_modifier)))
        else:
            output = round(pool / (match_number-(assumed_matches*slope_modifier)))
        if output < self.points_min:
            return self.points_min
        # Incase output is too large, return the max_points value.
        # Incase the output exceeds the given pool, return half the pool.
        if output > self.max_points_per_match:
           output = round(self.max_points_per_match)
        elif output > pool:
            output = round(pool/2)
        return output


if __name__ == '__main__':
    # Used for testing scenerios/flow
    gmech = Gmech(weekly_pool=500000, inactivity_time=5,inactivity_drop=0.40)
    poolAd = 500000
    for i in range(30):
        points = gmech.get_match_points(i,11,pool)
        pool -= points
        print 'Match#: %3i - Points Earned: %5i' % (i, points)