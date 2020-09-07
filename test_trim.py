from trim import TrimWords
import unittest

class TestTrimMethod(unittest.TestCase):
    def test_result(self):
        self.assertEqual(TrimWords('ini adalah tulisan yang sangat panjang',3),'ini adalah tulisan')

    def test_non_str(self):
        self.assertRaises(TypeError, TrimWords, 1234) 
    
    def test_empty(self):
        self.assertRaises(ValueError, TrimWords, 'ini adalah tulisan yang sangat panjang',1) 


if __name__ == "__main__":
    unittest.main()

