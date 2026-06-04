import unittest
# Import the functions from bmi.py
from bmi import findBMI

class TestCalculator(unittest.TestCase):

    # Test 1: Does it give correct BMI?
    def test_BMI(self):
        self.assertEqual(findBMI(1.8, 75), 23.15)

if __name__ == '__main__':
    unittest.main()