import unittest
from fooparam.core import complex_volume_calculation

class TestCalculateVolume(unittest.TestCase):
    def test_positive_radius(self):
        self.assertAlmostEqual(complex_volume_calculation(1), 4.1887902047863905)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            complex_volume_calculation(-1)

if __name__ == '__main__':
    unittest.main()
