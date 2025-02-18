import unittest
from main import is_armstrong

class TestArmstrongNumber(unittest.TestCase):
    def test_armstrong_numbers(self):
        self.assertTrue(is_armstrong(153))  # 1^3 + 5^3 + 3^3 = 153
        self.assertTrue(is_armstrong(9474)) # 9^4 + 4^4 + 7^4 + 4^4 = 9474
        self.assertTrue(is_armstrong(370))  # 3^3 + 7^3 + 0^3 = 370
    
    def test_non_armstrong_numbers(self):
        self.assertFalse(is_armstrong(123))
        self.assertFalse(is_armstrong(100))
        self.assertFalse(is_armstrong(9475))

if __name__ == "__main__":
    unittest.main()