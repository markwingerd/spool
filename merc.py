from gmech import Gmech

class Merc:
    """"""
    def __init__(self, gmech):
        """Initialize Merc variables."""
        self.gmech = gmech
        self.points = 0
        self.pool = 0
        self.this_weeks_pool = 0
        self.history = []

    def get_history(self, hours):
        """Manages merc history and returns the average hours."""
        # Update hours. self.history must not be larger than gmech.weeks_in_history
        self.history.append(hours)
        if len(self.history) > self.gmech.weeks_in_history:
            self.history.pop(0)
        # If all of self.history is 0 then re-init self.history to [].
        # Return 0 to avoid Div by 0.
        if sum(self.history) == 0:
            self.history = []
            return 0
        # Find the average hours in history.
        return sum(self.history)/float(len(self.history))

    # Method for dealing with reduced points for inactivity.


if __name__ == '__main__':
    gmech = Gmech()
    merc = Merc(gmech)