import unittest

from gmech import Gmech
from merc import Merc

class TestSpool(unittest.TestCase):
    """"""
    def test_gmech_init(self):
        """Tests the Init arguments."""
        gmech = Gmech()
        self.assertEqual(gmech.weekly_pool,gmech.weekly_pool)
        self.assertEqual(gmech.matches_per_hour,gmech.matches_per_hour)
        self.assertEqual(gmech.inactivity_time,gmech.inactivity_time)
        self.assertEqual(gmech.inactivity_drop,gmech.inactivity_drop)

    def test_merc_init(self):
        """Tests the internal variables."""
        gmech = Gmech()
        merc = Merc(gmech)
        self.assertEqual(merc.points,0)
        self.assertEqual(merc.pool,0)
        self.assertEqual(merc.this_weeks_pool,0)

    def test_pool_reduction(self):
        """Tests how point reduction works."""
        gmech = Gmech()
        self.assertEqual(gmech.get_point_reduction(hours=0, this_weeks_pool=100),20)
        self.assertEqual(gmech.get_point_reduction(hours=2.5, this_weeks_pool=100),10)
        self.assertEqual(gmech.get_point_reduction(hours=5, this_weeks_pool=100),0)
        self.assertEqual(gmech.get_point_reduction(hours=200, this_weeks_pool=100),0)

    def test_match_points_no_history(self):
        """Tests the point distribution for a mercs first week."""
        gmech = Gmech()
        self.assertEqual(gmech.get_match_points_no_history(0,300000),3000)
        self.assertEqual(gmech.get_match_points_no_history(10,300000),2800)
        self.assertEqual(gmech.get_match_points_no_history(100,300000),1000)
        self.assertEqual(gmech.get_match_points_no_history(101,300000),1000)

    def test_history(self):
        """Tests that a Merc history works."""
        gmech = Gmech()
        merc = Merc(gmech)
        self.assertEqual(merc.get_history(0),0)
        self.assertEqual(merc.get_history(20),20)
        self.assertEqual(merc.get_history(30),25)
        self.assertEqual(merc.get_history(10),20)
        self.assertEqual(merc.get_history(20),20)
        self.assertEqual(merc.get_history(0),10)
        self.assertEqual(merc.get_history(0),20/float(3))
        self.assertEqual(merc.get_history(0),0)
        self.assertEqual(merc.get_history(10),10)
        self.assertEqual(merc.get_history(20),15)
        self.assertEqual(merc.get_history(0),10)

if __name__ == '__main__':
    unittest.main()