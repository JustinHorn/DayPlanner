import unittest
import sys
import os
join = os.path.join
sys.path.append(join('./production/logic'))
from plan import Plan 
import ParseText

class Test_ParseEntries(unittest.TestCase):

    def test_one(self):
        text = "01:00 swimming\n02:00 jogging"
        entries = ParseText.parseTextToEntries(text)
        self.assertEqual("01:00", entries[0].start)
        self.assertEqual("01:00", entries[0].duration)
        self.assertEqual("swimming", entries[0].theme)


        self.assertEqual("02:00", entries[1].start)
        self.assertEqual("00:00", entries[1].duration)
        self.assertEqual("jogging", entries[1].theme)

    def test_makePlanEntries_duration(self):
        entry = ParseText.makePlanEntry("10:00 nah wie gehts? 00:05")
        self.assertEqual(entry.duration,"00:05")
        self.assertEqual(entry.start,"10:00")
        self.assertEqual(entry.theme,"nah wie gehts? ")
    
    def test_makePlanEntries(self):
        entry = ParseText.makePlanEntry("10:00 nah wie gehts? ")
        self.assertEqual(entry.duration,"00:00")
        self.assertEqual(entry.start,"10:00")
        self.assertEqual(entry.theme,"nah wie gehts? ")



if __name__=="__main__":
    unittest.main()