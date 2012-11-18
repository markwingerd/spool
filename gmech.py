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
        if this_weeks_pool < 0:
            return 0
        if hours < self.inactivity_time:
            slope = -1 * self.inactivity_drop / self.inactivity_time
            penalty = slope * hours + self.inactivity_drop
            #print 'REDUCE --- Pool: %7i - Factor: %5.2f - Reduce: %6i' % (this_weeks_pool, penalty, round(this_weeks_pool * penalty))
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
        slope_modifier=0.9 # Controls the degrade of SP over time. This is primarily used for the first phase of this function so the pool isn't completely consumed.
        output = 0
        #assumed_matches = history * 1.5 * self.matches_per_hour
        assumed_matches = history * self.matches_per_hour #A multiplier extends the initial point value over more matches as well as lowering the point value give.
        # Within the assumed_matches, return a standard point value. Beyond
        # assumed_matches, return a deteriorating point value.
        if match_number < assumed_matches:
            #output = round(pool / (1.5*assumed_matches-match_number))
            output = round(pool / (assumed_matches-match_number*0.90)) #Attach *0.95 to match_number to get a 10% degrade.
        else:
            output = round(pool / (match_number-assumed_matches*0.90))
        # Slope should not be positive. Returning min_points is sufficent.
        # If output is too low, return the minimum points gained.
        if output < self.points_min:
            #print 'low out'
            return self.points_min
        # fdsfds
        elif output*self.inactivity_time*self.matches_per_hour > self.weekly_pool:
            #print 'SERIOUSLY'
            return round(self.weekly_pool / (self.inactivity_time*self.matches_per_hour))
         # Incase output is ever larger than the pool, Return half the pool. (Handles a rare error with very small histories.)
        elif output > pool:
            #print 'round(pool/2)', round(pool/2)
            return round(pool/2)
        #print 'Normal: ', output
        return output


if __name__ == '__main__':
    # Used for testing scenerios/flow
    gmech = Gmech()
    pool = 548142
    for i in range(12*2):
        points = gmech.get_match_points(i,float(4)/3,pool)
        pool -= points
        print '%3i - Points: %5i - Pool: %6i' % (i, points, pool)