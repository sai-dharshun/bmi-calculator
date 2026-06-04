import unittest
# Import the functions from your calc.py file
from bmi import findBMI

class TestCalculator(unittest.TestCase):

    # Test 1: Does addition work?
    def test_BMI(self):
        self.assertEqual(findBMI(1.8, 75), 23.15)

if __name__ == '__main__':
    unittest.main()