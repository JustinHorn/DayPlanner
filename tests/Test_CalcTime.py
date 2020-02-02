import unittest
import sys
import os
sys.path.append(os.path.join('./production/logic'))
import CalcTime 

class Test_CalcTime(unittest.TestCase):

    def test_timeEquals(self):
        self.assertEqual("07:00","07:00")

    def test_timeAdd(self):
        self.assertEqual("07:33",CalcTime.addTime("07:00","00:33"))
        self.assertEqual("00:33",CalcTime.addTime("07:00","17:33"))
        self.assertEqual("08:02",CalcTime.addTime("07:29","00:33"))

    def test_timeSubtract(self):
        self.assertEqual("06:27",CalcTime.substractTime("07:00","00:33"))
        self.assertEqual("13:27",CalcTime.substractTime("07:00","17:33"))
        self.assertEqual("06:56",CalcTime.substractTime("07:29","00:33"))

if __name__ == '__main__': 
    unittest.main()

