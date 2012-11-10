import unittest

from gmech import Gmech
from merc import Merc

class TestSpool(unittest.TestCase):
    """"""
    def test_weekly_pool(self):
        """Tests if the initial weekly pool is within range."""
        gmech = Gmech(inactivity_drop=0)
        average_merc = Merc(gmech)
        average_merc.week()
        self.assertEqual(average_merc.this_weeks_pool, 300000)

        
    def test_weekly_inactivity_drop(self):
        """ Tests what happens to a mercs pool if they don't play for a week. """
        gmech = Gmech()
        inactive_merc = Merc(gmech)
        inactive_merc.week()
        self.assertEqual(inactive_merc.pool, 240000)

    #def test_point_output(self):
        """Tests the amount of points given depending on the match number."""
        #gmech = Gmech()
        #self.assertEqual(gmech.get_match_points(1),10000)
        #self.assertEqual(gmech.get_match_points(30),gmech.get_match_points(30))
        #self.assertEqual(gmech.get_match_points(100),gmech.get_match_points(100))



if __name__ == '__main__':
    unittest.main()