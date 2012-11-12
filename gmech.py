import math

class Gmech:
    """"""
    def __init__(self, weekly_pool=300000, matches_per_hour=3, inactivity_time=5, inactivity_drop=0.20):
        # Init for all mech variables.
        self.weekly_pool = weekly_pool
        self.matches_per_hour = matches_per_hour
        self.inactivity_time = inactivity_time
        self.inactivity_drop = inactivity_drop
    # Get weekly pool.
    # Get match points based on match number and total pool.
    # Get point reduction for low weekly hours.

if __name__ == '__main__':
    # Used for testing scenerios/flow
    gmech = Gmech()
    print gmech.weekly_pool