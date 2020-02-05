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


if __name__=="__main__":
    unittest.main()