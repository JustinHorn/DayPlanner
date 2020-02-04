import unittest
import sys
import os
join = os.path.join
sys.path.append(join('./production/logic'))
import CalcTime 
import Load 
from plan import Plan 
from template import Template
import TestHelper
import Change
import ParseText

class Test_Change(unittest.TestCase):

    test_source = join("material/test/test_template_1.txt")

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = Load.loadTemplate(Test_Change.test_source)

    def test_entriesToTemplate(self):
        #test only entries
        p,e = TestHelper.createPlan(self,"ESE2")
        l = p.step_list
        l = Change.formatList(l)
        self.assertEqual(len(l),1)
        self.assertEqual(len(l[0].step_list),3)
        self.assertEqual(l[0].step_list[0],e)

        #test entrie,template,entrie
        p,e = TestHelper.createPlan(self,"ESTE")
        l = p.step_list
        l = Change.formatList(l)
        self.assertEqual(len(l),3)
        self.assertEqual(l[1],self.template)
        self.assertEqual(l[0],e)

        #test entries,template,entries
        p,e = TestHelper.createPlan(self,"ESETE2")

        l = p.step_list
        l = Change.formatList(l)
        self.assertEqual(len(l[2].step_list),2)
        self.assertEqual(l[1],self.template)
        self.assertEqual(l[0].step_list[0],e)

        #test template,entrie,template
        p,e = TestHelper.createPlan(self,"TEST")

        l = p.step_list
        l = Change.formatList(l)
        self.assertEqual(len(l),3)
        self.assertEqual(l[0],self.template)
        self.assertEqual(l[2],self.template)
        
        #test template, entries,template
        p,e = TestHelper.createPlan(self,"TESE2T")

        l = p.step_list
        l = Change.formatList(l)
        self.assertEqual(len(l),3)
        self.assertEqual(l[0],self.template)
        self.assertEqual(l[2],self.template)

    def test_mergeListToEntries(self):
        p,e = TestHelper.createPlan(self,"T")
        t = p.step_list
        entries = ParseText.parseTextToEntries(Load.loadData(join("material/test/test_update1.txt")))
        new_list = Change.mergeListToEntries(t,entries)
        self.assertEqual(t[0],new_list[0])

    def test_doesEntryListContain(self):
        p,e = TestHelper.createPlan(self,"T")
        t = p.step_list
        entries = ParseText.parseTextToEntries(Load.loadData(join("material/test/test_update1.txt")))
        contains,index = Change.doesEntryListContain(t[0],entries)
        self.assertEqual(index,0)

if __name__=="__main__":
    unittest.main()