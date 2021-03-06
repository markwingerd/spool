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
        # Variables to store and display stats
        self.weekly_outcome = []
        self.weekly_points = []

    def add_history(self, hours):
        """Adds a week of hours to history."""
        self.history.append(hours)
        # self.history must not be larger than gmech.weeks_in_history
        if len(self.history) > self.gmech.weeks_in_history:
            self.history.pop(0)
        # If all of self.history is 0 then re-init self.history to [].
        if sum(self.history) == 0:
            self.history = []

    def get_history(self):
        """Manages merc history and returns the average hours."""
        # Return 0 to avoid Div by 0.
        if len(self.history) == 0:
            return 0
        # Find the average hours in history.
        return sum(self.history)/float(len(self.history))

    def week(self, hours_played):
        """Apply matches for a week."""
        # Initialize this week.
        matches_played = hours_played * gmech.matches_per_hour
        self.this_weeks_pool = self.gmech.weekly_pool
        # Get points for each match. Choose correct function based on history.
        if self.history:
            for i in range(matches_played):
                match_points = int(self.gmech.get_match_points(i,self.get_history(),self.pool+self.this_weeks_pool))
                self.points += match_points
                self.this_weeks_pool -= match_points
                self.record_weekly_points(match_points)
        else:
            for i in range(matches_played):
                match_points = int(self.gmech.get_match_points_no_history(i,self.pool+self.this_weeks_pool))
                self.points += match_points
                self.this_weeks_pool -= match_points
                self.record_weekly_points(match_points)
        # Finalize the week.
        self.add_history(hours_played)
        self.this_weeks_pool -= self.gmech.get_point_reduction(hours_played,self.this_weeks_pool)
        self.pool += self.this_weeks_pool
        #print 'Matches: %3i - Points gained: %10.1f - Pool left: %10.1f - Average points: %7.1f' % (matches_played, self.points, self.pool, average_points)
        self.record_weekly_outcome(matches_played, self.get_history(), self.points, self.pool)
        return 0

    def record_weekly_outcome(self, matches_played, average_history, points_gained, pool_left):
        average_points = sum(self.weekly_points[len(self.weekly_outcome)])/float(matches_played)
        week_tuple = (len(self.weekly_outcome)+1,
            matches_played,
            average_history,
            points_gained,
            pool_left,
            average_points )
        self.weekly_outcome.append(week_tuple)

    def record_weekly_points(self, match_points):
        if len(self.weekly_points) <= len(self.weekly_outcome):
            self.weekly_points.append([])
        self.weekly_points[len(self.weekly_outcome)].append(match_points)

    def show_weekly_outcome(self):
        for item in self.weekly_outcome:
            print 'Week: {:>2} - Matches Played: {:>3} - Average Hours: {:>2.0f} - Points Gained: {:>10.0f} - Pool Left: {:>10.0f} - Average Points: {:>10.1f}'.format(item[0], item[1], item[2], item[3], item[4], item[5])

    def get_weekly_points(self, week):
        return self.weekly_points[week-1]

def week_comparison(col1, col2, col3, col4):
    points = map(None, col1, col2, col3, col4)
    print 'Match{:_>4}:{:_>10}{:_>10}{:_>10}{:_>10}'.format('#', 'Merc1', 'Merc2', 'Merc3', 'Merc4')
    for i, item in enumerate(points):
        print 'Match{:_>4}:{:_>10}{:_>10}{:_>10}{:_>10}'.format(i+1, item[0], item[1], item[2], item[3])


if __name__ == '__main__':
    gmech = Gmech(weekly_pool=500000, inactivity_time=5,inactivity_drop=0.40)
    addicted_merc = Merc(gmech)
    addicted_merc.week(28)
    addicted_merc.week(34)
    addicted_merc.week(31)
    addicted_merc.week(34)
    addicted_merc.week(20)
    addicted_merc.week(23)
    addicted_merc.week(19)
    addicted_merc.week(37)
    addicted_merc.week(38)
    addicted_merc.week(35)
    addicted_merc.week(39)
    addicted_merc.week(52)
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
    casual_merc = Merc(gmech)
    casual_merc.week(3)
    casual_merc.week(4)
    casual_merc.week(2)
    casual_merc.week(4)
    casual_merc.week(1)
    casual_merc.week(1)
    casual_merc.week(1)
    casual_merc.week(2)
    casual_merc.week(4)
    casual_merc.week(2)
    casual_merc.week(3)
    casual_merc.week(2)
    inactive_merc = Merc(gmech)
    inactive_merc.week(1)
    inactive_merc.week(1)
    inactive_merc.week(1)
    inactive_merc.week(1)
    inactive_merc.week(1)
    inactive_merc.week(1)
    inactive_merc.week(1)
    inactive_merc.week(1)
    inactive_merc.week(1)
    inactive_merc.week(1)
    inactive_merc.week(1)
    inactive_merc.week(1)

    print 'Addicted Merc'
    addicted_merc.show_weekly_outcome()
    print 'Average Merc'
    average_merc.show_weekly_outcome()
    print 'Casual Merc'
    casual_merc.show_weekly_outcome()
    print 'Inactive Merc'
    inactive_merc.show_weekly_outcome()

    week_comparison(addicted_merc.get_weekly_points(6),
        average_merc.get_weekly_points(6),
        casual_merc.get_weekly_points(6),
        inactive_merc.get_weekly_points(6),
        )