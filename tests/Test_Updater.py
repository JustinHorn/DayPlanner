import unittest
import sys
import os
join = os.path.join
sys.path.append(join('./production/logic'))
import load 
from plan import Plan 
from template import Template
from entry import Entry
import TestHelper
import ParseText

from updater import Updater

#TODO: needs imporeved testing!
class Test_Updater(unittest.TestCase):

    test_source = join("material/test/test_template_1.txt")

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = load.loadTemplate(Test_Updater.test_source)

    def test_mergeListToEntries(self):
        p,e = TestHelper.createPlan(self,"T")
        t = p.step_list
        entries = ParseText.parseTextToEntries(load.loadText(join("material/test/test_update1.txt")))
        
        u = Updater(t,entries)
        new_list = u.mergeListToEntries()
        self.assertEqual(t[0],new_list[0])

    def test_doesEntryListContain(self):
        p,e = TestHelper.createPlan(self,"T")
        t = p.step_list
        entries = ParseText.parseTextToEntries(load.loadText(join("material/test/test_update1.txt")))
        
        u = Updater(t,entries)
        contains,index = u.doesEntryListContain(t[0])
        
        self.assertEqual(index,0)

    def test_update(self):
        p,e = TestHelper.createPlan(self,"T")
        t = p.step_list
        entries = [Entry("00:10","nah wie gehts?")]
        step_list =  Updater(t,entries).update()
        self.assertEqual(step_list,entries)


if __name__=="__main__":
    unittest.main()