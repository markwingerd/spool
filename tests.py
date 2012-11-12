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
        merc = Merc()
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

if __name__ == '__main__':
    unittest.main()