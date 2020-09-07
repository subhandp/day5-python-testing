from leap_year import isLeapYear
import unittest

class TestLeapYearMethod(unittest.TestCase):
    def test_result_kabisat(self):
        self.assertEqual(isLeapYear(2000), "Kabisat")

    def test_result_not_kabisat(self):
        self.assertEqual(isLeapYear(1900), "Bukan kabisat")
    
    def test_non_int(self):
        self.assertRaises(TypeError, isLeapYear, "2000") 

if __name__ == "__main__":
    unittest.main()

