from length import leng
import unittest

class TestStringLenMethod(unittest.TestCase):
    def test_result(self):
        self.assertEqual(leng('subhan'),6)
    def test_result_space(self):
        self.assertEqual(leng('subhan dinda putra'),18)
    def test_non_str(self):
        self.assertRaises(TypeError, leng, 1234) 

if __name__ == "__main__":
    unittest.main()

