import unittest
import sys
import os
join = os.path.join
sys.path.append(join('./production/logic'))
from plan import Plan 
from entry import Entry 
from routine import Routine
import ParseText
import re

class Test_ParseEntries(unittest.TestCase):

    def test_one(self):
        text = "01:00 swimming\n02:00 jogging"
        entries = ParseText.planText_toEntries(text)
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

    
    def test_insertTime(self):
        test_source = """00:01 hi wie gehts?

        00:03 mir gehts gut!"""
        plan= Plan("heute")
        plan.add(Entry("00:02","hi wie gehts?",start="00:01"))
        plan.add(Entry("00:05","mir gehts gut!",start="00:03"))

        string = ParseText.insertEndTime( plan,test_source,1)  
        string = string.split("\n")
        l = test_source.split("\n")
        self.assertEqual(len(string),len(l))
        self.assertEqual(l[0],string[0])
        self.assertNotEqual(l[1],string[1])
        self.assertEqual(string[1].strip(),"00:03")
        self.assertEqual(l[2],string[2])

    def test_insertTimeWithTemplates(self):
        test_source = """00:01 hi wie gehts?\n00:03 mir gehts gut!
        """
        plan= Plan("heute")
        r = Routine("test")
        r.add(Entry("00:02","hi wie gehts?",start="00:01"))
        r.add(Entry("00:05","mir gehts gut!",start="00:03"))
        plan.add(r)
        plan.updateStarts("00:01",0)


        string = ParseText.insertEndTime( plan,test_source,2)  
        string = string.split("\n")
        l = test_source.split("\n")
        self.assertEqual(len(string),len(l))
        self.assertEqual(l[0],string[0])
        self.assertEqual(string[1],l[1])
        self.assertEqual(string[2].strip(),"00:08")
        self.assertNotEqual(l[2],string[2])



if __name__=="__main__":
    unittest.main()