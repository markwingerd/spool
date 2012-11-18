from gmech import Gmech

class Merc:
    """"""
    def __init__(self, gmech):
        """Initialize Merc variables."""
        self.gmech = gmech
        self.points = 0
        self.this_weeks_pool = 0
        self.pool = 0
        self.history = []

    def add_history(self, hours):
        """Adds a week of hours to history."""
        self.history.append(hours)
        # self.history must not be larger than gmech.weeks_in_history
        if len(self.history) > self.gmech.weeks_in_history:
            self.history.pop(0)

    def get_history(self):
        """Manages merc history and returns the average hours."""
        # If all of self.history is 0 then re-init self.history to [].
        # Return 0 to avoid Div by 0.
        if sum(self.history) == 0:
            self.history = []
            return 0
        # Find the average hours in history.
        return sum(self.history)/float(len(self.history))

    def week(self, hours_played):
        """Apply matches for a week."""
        # Initialize this week.
        matches_played = hours_played * gmech.matches_per_hour
        average_points = 0 ###
        self.this_weeks_pool = self.gmech.weekly_pool
        # Get points for each match. Choose correct function based on history.
        if self.history:
            for i in range(matches_played):
                match_points = self.gmech.get_match_points(i,self.get_history(),self.pool+self.this_weeks_pool)
                self.points += match_points
                self.this_weeks_pool -= match_points
                average_points += match_points ###
            average_points /= matches_played ###
        else:
            for i in range(matches_played):
                match_points = self.gmech.get_match_points_no_history(i,self.pool+self.this_weeks_pool)
                self.points += match_points
                self.this_weeks_pool -= match_points
                average_points += match_points ###
            average_points /= matches_played ###
        # Finalize the week.
        self.add_history(hours_played) # History needs to be updated AFTER the week.
        self.this_weeks_pool -= self.gmech.get_point_reduction(hours_played,self.this_weeks_pool)
        self.pool += self.this_weeks_pool
        print 'Matches: %3i - Points gained: %10.1f - Pool left: %10.1f - Average points: %7.1f' % (matches_played, self.points, self.pool, average_points)

#NEGATIVE POOL GOING TO REDUCTION. FIX
if __name__ == '__main__':
    gmech = Gmech(weekly_pool=500000, inactivity_time=10,inactivity_drop=0.40)
    print 'Addicted Merc'
    average_merc = Merc(gmech)
    average_merc.week(28)
    average_merc.week(34)
    average_merc.week(31)
    average_merc.week(34)
    average_merc.week(20)
    average_merc.week(23)
    average_merc.week(19)
    average_merc.week(37)
    average_merc.week(38)
    average_merc.week(35)
    average_merc.week(39)
    average_merc.week(52)
    print 'Average Merc'
    average_merc = Merc(gmech)
    average_merc.week(12)
    average_merc.week(14)
    average_merc.week(11)
    average_merc.week(9)
    average_merc.week(13)
    average_merc.week(12)
    average_merc.week(12)
    average_merc.week(8)
    average_merc.week(10)
    average_merc.week(10)
    average_merc.week(14)
    average_merc.week(12)
    print 'Casual Merc'
    average_merc = Merc(gmech)
    average_merc.week(3)
    average_merc.week(4)
    average_merc.week(2)
    average_merc.week(4)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(2)
    average_merc.week(4)
    average_merc.week(2)
    average_merc.week(3)
    average_merc.week(2)
    print 'Inactive Merc'
    average_merc = Merc(gmech)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)
    average_merc.week(1)