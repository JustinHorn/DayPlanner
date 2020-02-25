import unittest
import sys
import os
join = os.path.join
sys.path.append(join('./production/logic'))
import load 
from plan import Plan 
from routine import Routine
from entry import Entry
import TestHelper
import ParseText

from updater import Updater

#TODO: needs imporeved testing!
class Test_Updater(unittest.TestCase):

    test_source = join("material/test/test_template_1.txt")

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.routine = load.loadRoutine(Test_Updater.test_source)

    def test_mergeListToEntries(self):
        p,e = TestHelper.createPlan(self,"R")
        r = p.step_list
        entries = ParseText.planText_toEntries(load.loadText(join("material/test/test_update1.txt")))
        
        u = Updater(r,entries)
        new_list = u.mergeListToEntries()
        self.assertEqual(r[0],new_list[0])

    def test_doesEntryListContain(self):
        p,e = TestHelper.createPlan(self,"R")
        r = p.step_list
        entries = ParseText.planText_toEntries(load.loadText(join("material/test/test_update1.txt")))
        
        u = Updater(r,entries)
        contains,index = u.doesEntryListContain(r[0])
        
        self.assertEqual(index,0)

    def test_update(self):
        p,e = TestHelper.createPlan(self,"R")
        r = p.step_list
        entries = [Entry("00:10","nah wie gehts?")]
        step_list =  Updater(r,entries).update()
        self.assertEqual(step_list,entries)


if __name__=="__main__":
    unittest.main()