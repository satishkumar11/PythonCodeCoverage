# test/test_statistics.py

import unittest
from code.statistics import mean, median, mode

class TestStatistics(unittest.TestCase):

    def test_mean(self):
        # Test cases for mean function
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(mean([1.5, 2.5, 3.5, 4.5]), 3.0)

    def test_median(self):
        # Test cases for median function
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_mode(self):
        # Test cases for mode function
        self.assertEqual(mode([1, 2, 2, 3, 4]), 2)
        self.assertEqual(mode([1, 2, 2, 3, 3, 4]), [2, 3])

if __name__ == '__main__':
    unittest.main()
