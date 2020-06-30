import unittest
import lineslope


class TestLineSlope(unittest.TestCase):

    def test_lineslope(self):  
        self.assertEqual(lineslope.ys(10, 5), 5)
        self.assertEqual(lineslope.xs(10, 5), 5)



if __name__ == "__main__":
    unittest.main()
    pass