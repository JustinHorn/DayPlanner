import unittest
import sys
sys.path.append('.\\production\\')
import calcTime 

class Test_Time(unittest.TestCase):

    def test_timeEquals(self):
        self.assertEqual("07:00","07:00")

    def test_timeAdd(self):
        self.assertEqual("07:33",calcTime.addTime("07:00","00:33"))
        self.assertEqual("00:33",calcTime.addTime("07:00","17:33"))
        self.assertEqual("08:02",calcTime.addTime("07:29","00:33"))

    def test_timeSubtract(self):
        self.assertEqual("06:27",calcTime.substractTime("07:00","00:33"))
        self.assertEqual("13:27",calcTime.substractTime("07:00","17:33"))
        self.assertEqual("06:56",calcTime.substractTime("07:29","00:33"))

if __name__ == '__main__': 
    unittest.main()