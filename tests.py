import unittest

from gmech import Gmech

class TestSpool(unittest.TestCase):
    """"""
    def test_gmech_init(self):
        """Tests the Init arguments."""
        gmech = Gmech()
        self.assertEqual(gmech.weekly_pool,gmech.weekly_pool)
        self.assertEqual(gmech.matches_per_hour,gmech.matches_per_hour)
        self.assertEqual(gmech.inactivity_time,gmech.inactivity_time)
        self.assertEqual(gmech.inactivity_drop,gmech.inactivity_drop)

if __name__ == '__main__':
    unittest.main()