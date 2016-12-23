import unittest
from app import *

class TestSuite(unittest.TestCase):

    def test_parse_s(self):
        self.assertEquals(parse('1s').seconds(), 1)

    def test_parse_m(self):
        self.assertEquals(parse('23m').minutes(), 23)
    
    def test_parse_h(self):
        self.assertEquals(parse('19h').minutes(), 19 * 60)

    def test_parse_d(self):
        self.assertEquals(parse('3d').days(), 3)

    def test_parse_w(self):
        self.assertEquals(parse('2w').hours(), 14 * 24)


    def test_parse_y(self):
        self.assertEquals(parse('75y').years(), 75)

    def test_invalid(self):
        self.assertRaises(Exception, parse, '1.5d')

if __name__ == '__main__':
    unittest.main()