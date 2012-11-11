import unittest

from gmech import Gmech
from merc import Merc

class TestSpool(unittest.TestCase):
    """"""
    def test_weekly_pool(self):
        """Tests if the initial weekly pool is within range."""
        gmech = Gmech(inactivity_drop=0)
        average_merc = Merc(gmech)
        average_merc.play()
        self.assertEqual(average_merc.this_weeks_pool, 300000)

        
    def test_weekly_inactivity_drop(self):
        """ Tests what happens to a mercs pool if they don't play for a week. """
        gmech = Gmech()
        inactive_merc = Merc(gmech)
        inactive_merc.play()
        self.assertEqual(inactive_merc.pool, 240000)

    def test_point_output(self):
        """Tests the amount of points given depending on the match number."""
        gmech = Gmech()
        self.assertEqual(gmech.get_match_points(0, 0),5000)
        self.assertEqual(gmech.get_match_points(0, 25),4000)
        self.assertEqual(gmech.get_match_points(0, 50),3000)
        self.assertEqual(gmech.get_match_points(0, 99),1040)
        self.assertEqual(gmech.get_match_points(0, 200),1000)

    def test_point_gain(self):
        """Tests how a merc gains points"""
        gmech = Gmech()
        # First Week
        average_merc = Merc(gmech)
        average_merc.play(1)
        self.assertGreater(average_merc.points, 14000)
        self.assertLess(average_merc.points, 15000)
        self.assertGreater(average_merc.pool, 285000*0.80)
        self.assertLess(average_merc.pool, 286000*0.80)
        # Second Week
        average_merc.play(7)
        self.assertGreater(average_merc.points, 14000+96000)
        self.assertLess(average_merc.points, 15000+100000)
        self.assertGreater(average_merc.pool, (285000*0.80)+200000)
        self.assertLess(average_merc.pool, (286000*0.80)+300000)


    def test_time_recording(self):
        """Tests if the game is recording a mercs play time."""
        gmech = Gmech()
        inactive_merc = Merc(gmech)
        average_merc = Merc(gmech)
        great_merc = Merc(gmech)
        # First Week
        inactive_merc.play(5)
        average_merc.play(10)
        great_merc.play(25)
        # Second Week
        inactive_merc.play(1)
        average_merc.play(8)
        great_merc.play(35)
        self.assertEqual(inactive_merc.assumed_weekly_hours, 3)
        self.assertEqual(average_merc.assumed_weekly_hours, 9)
        self.assertEqual(great_merc.assumed_weekly_hours, 30)



if __name__ == '__main__':
    unittest.main()