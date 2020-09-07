from num_to_words import convert
import unittest

class TestStringLenMethod(unittest.TestCase):
    def test_result(self):
        self.assertEqual(convert(1),"satu ")
    def test_result_second(self):
        self.assertEqual(convert(12),"duabelas ")
    def test_result_third(self):
        self.assertEqual(convert(13),"tigabelas ")

if __name__ == "__main__":
    unittest.main()

