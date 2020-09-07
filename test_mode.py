from mode import Mode
import unittest

class TestLeapYearMethod(unittest.TestCase):
    def test_result_first(self):
        self.assertEqual(Mode([1,2,3,4,5,6,6,8,8,6,9]), 6)

    def test_result_second(self):
        self.assertEqual(Mode([87.5, 88.5, 60.5, 90.5, 88.5]), 88.5)

if __name__ == "__main__":
    unittest.main()

