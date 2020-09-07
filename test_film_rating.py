from film_rating import film_rating
import unittest

class TestLeapYearMethod(unittest.TestCase):
    def test_result_film_rating(self):
        self.assertEqual(film_rating(15), "REMAJA")
        self.assertEqual(film_rating(32), "DEWASA")

    def test_non_int(self):
        self.assertRaises(TypeError, film_rating, "15") 

if __name__ == "__main__":
    unittest.main()

