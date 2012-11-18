import unittest

from gmech import Gmech
from merc import Merc
# 151000 pass - ~500000 Active
class TestSpool(unittest.TestCase):
    """"""
    def setUp(self):
        """"""
        self.gmech = Gmech()
        self.merc = Merc(self.gmech)

    def test_gmech_init(self):
        """Tests the Init arguments."""
        self.assertEqual(self.gmech.weekly_pool,300000)
        self.assertEqual(self.gmech.matches_per_hour,3)
        self.assertEqual(self.gmech.inactivity_time,5)
        self.assertEqual(self.gmech.inactivity_drop,0.20)
        self.assertEqual(self.gmech.points_min,1000)
        self.assertEqual(self.gmech.max_matches,100)
        self.assertEqual(self.gmech.weeks_in_history,3)

    def test_merc_init(self):
        """Tests the internal variables."""
        self.assertEqual(self.merc.points,0)
        self.assertEqual(self.merc.pool,0)
        self.assertEqual(self.merc.this_weeks_pool,0)
        self.assertEqual(self.merc.history,[])

    def test_pool_reduction(self):
        """Tests how point reduction works."""
        self.assertEqual(self.gmech.get_point_reduction(hours=0, this_weeks_pool=100),20)
        self.assertEqual(self.gmech.get_point_reduction(hours=2.5, this_weeks_pool=100),10)
        self.assertEqual(self.gmech.get_point_reduction(hours=5, this_weeks_pool=100),0)
        self.assertEqual(self.gmech.get_point_reduction(hours=200, this_weeks_pool=100),0)

    def test_match_points_no_history(self):
        """Tests the point distribution for merc with no history."""
        self.assertEqual(self.gmech.get_match_points_no_history(0,300000),3000)
        self.assertEqual(self.gmech.get_match_points_no_history(10,300000),2800)
        self.assertEqual(self.gmech.get_match_points_no_history(100,300000),1000)
        self.assertEqual(self.gmech.get_match_points_no_history(101,300000),1000)

    def test_match_points_with_history(self):
        """Tests the point distribution for merc with a history."""
        self.assertEqual(self.gmech.get_match_points(0, 10, 500000), 16667)
        self.assertEqual(self.gmech.get_match_points(1, 10, 483333), 16609)
        self.assertEqual(self.gmech.get_match_points(29, 10, 51143), 13114)
        self.assertEqual(self.gmech.get_match_points(30, 10, 38029), 12676)
        self.assertEqual(self.gmech.get_match_points(31, 10, 25353), 6338)
        self.assertEqual(self.gmech.get_match_points(36, 10, 9508), 1056)
        self.assertEqual(self.gmech.get_match_points(37, 10, 7452), 1000)
        self.assertEqual(self.gmech.get_match_points(46, 10, -548), 1000)

    def test_history(self):
        """Tests that a Merc history works."""
        self.merc.add_history(0)
        self.assertEqual(self.merc.get_history(),0)
        self.merc.add_history(20)
        self.assertEqual(self.merc.get_history(),20)
        self.merc.add_history(30)
        self.assertEqual(self.merc.get_history(),25)
        self.merc.add_history(10)
        self.assertEqual(self.merc.get_history(),20)
        self.merc.add_history(20)
        self.assertEqual(self.merc.get_history(),20)
        self.merc.add_history(0)
        self.assertEqual(self.merc.get_history(),10)
        self.merc.add_history(0)
        self.assertEqual(self.merc.get_history(),20/float(3))
        self.merc.add_history(0)
        self.assertEqual(self.merc.get_history(),0)
        self.merc.add_history(10)
        self.assertEqual(self.merc.get_history(),10)
        self.merc.add_history(20)
        self.assertEqual(self.merc.get_history(),15)
        self.merc.add_history(0)
        self.assertEqual(self.merc.get_history(),10)


if __name__ == '__main__':
    unittest.main()