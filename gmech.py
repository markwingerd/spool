import math

class Gmech:
    """"""
    def __init__(self, weekly_pool=300000, matches_per_hour=3,
                 inactivity_time=5, inactivity_drop=0.20, points_min=1000,
                 max_matches=100, weeks_in_history=3):
        """Init for all mech variables."""
        self.weekly_pool = weekly_pool
        self.matches_per_hour = matches_per_hour
        self.inactivity_time = inactivity_time
        self.inactivity_drop = inactivity_drop
        self.weeks_in_history = weeks_in_history
        # points_min only applies to get_match_points_no_history.
        self.points_min = points_min
        self.max_matches = max_matches

    def get_point_reduction(self, hours, this_weeks_pool):
        """Returns points that will be subtracted from a weekly pool."""
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
        points_max = round(pool/self.max_matches)
        slope = -1 * ((points_max-self.points_min)/self.max_matches)
        output = round((slope * match_number) + points_max)
        # Slope should not be positive. Returning min_points is sufficent.
        # If output is too low, return the minimum points gained.
        if (slope > 0) or (output < self.points_min):
            return self.points_min
        return output

    def get_match_points(self, match_number, history, pool):
        """Returns the points for the match_number. Warning: Equations still 
        need to be studied."""
        unknown=1.5 # I don't know what this does but its good.
        output = 0
        slope = 0
        assumed_matches = history * unknown * self.matches_per_hour
        # Within the assumed_matches, return a standard point value. Beyond
        # assumed_matches, return a deteriorating point value.
        if match_number < assumed_matches:
            output = round(pool / (unknown*assumed_matches-match_number))
        else:
            points_max = round(pool/assumed_matches*2)
            slope = -1 * ((points_max-self.points_min)/assumed_matches)
            output = round(slope * (match_number-assumed_matches)) + points_max
        # Slope should not be positive. Returning min_points is sufficent.
        # If output is too low, return the minimum points gained.
        if (slope > 0) or (output < self.points_min):
            return self.points_min
        return output


if __name__ == '__main__':
    # Used for testing scenerios/flow
    gmech = Gmech()
    pool = 400000
    for i in range(100):
        points = gmech.get_match_points(i,10,pool)
        pool -= points
        print '%3i - Points: %4i - Pool: %6i' % (i, points, pool)