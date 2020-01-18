import unittest
import sys
sys.path.append('.\\production\\logic')
import calcTime 
import load 
from entry import Entry 
from plan import Plan 
from template import Template
import TestHelper

class Test_Plan(unittest.TestCase):

    test_source = "material\\test\\test_template_1.txt"

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = load.loadTemplate(Test_Plan.test_source)


    def test_addToPlan(self):
        p,e = TestHelper.createPlan(self,"ETE")

        step_list = p.step_list
        self.assertEqual(step_list[0].start,Plan.STANDARD_START)
        self.assertEqual(step_list[1].start,calcTime.addTime(Plan.STANDARD_START,step_list[0].duration))
        self.assertEqual(step_list[2].start,calcTime.addTime(step_list[1].start,step_list[1].duration))
    
    def test_removeElement(self):
        p = TestHelper.createPlan(self,"TTT")

        self.assertNotEqual(Plan.STANDARD_START,p.step_list[1].start)
        self.assertEqual(3,len(p.step_list))
        end = p.end

        p.remove(0)
        self.assertEqual(Plan.STANDARD_START,p.step_list[0].start)
        self.assertEqual(2,len(p.step_list))
        self.assertNotEqual(end,p.end)

    def test_removeElement(self):
        t1 = self.template.clone()
        t2 = self.template.clone()
 
        p = Plan("Today")
        p.add(t1)
        p.add(self.template)
        p.add(t2)
        
        endBefore = p.end
        p.splitTemplate(1,2)

        self.assertEqual(endBefore,p.end)
        self.assertEqual(len(p.step_list),4)
        self.assertEqual(p.step_list[0].theme,t1.theme)
        self.assertEqual(p.step_list[3].theme,t2.theme)

    def test_pEqual(self):
        p1 = Plan("1")
        p2 = Plan("2")

        p1.add(self.template)
        p2.add(self.template)

        self.assertEqual(p1,p2)
        self.assertNotEqual(id(p1),id(p2))


    


    def test_entriesToTemplate(self):
        #test only entries
        p,e = TestHelper.createPlan(self,"ESE2")
        l = p.step_list
        l = Plan.formatList(l)
        self.assertEqual(len(l),1)
        self.assertEqual(len(l[0].step_list),3)
        self.assertEqual(l[0].step_list[0],e)


        #test entrie,template,entrie
        p,e = TestHelper.createPlan(self,"ESTE")
        l = p.step_list
        l = Plan.formatList(l)
        self.assertEqual(len(l),3)
        self.assertEqual(l[1],self.template)
        self.assertEqual(l[0],e)

        #test entries,template,entries
        p,e = TestHelper.createPlan(self,"ESETE2")

        l = p.step_list
        l = Plan.formatList(l)
        self.assertEqual(len(l[2].step_list),2)
        self.assertEqual(l[1],self.template)
        self.assertEqual(l[0].step_list[0],e)

        #test template,entrie,template
        p,e = TestHelper.createPlan(self,"TEST")

        l = p.step_list
        l = Plan.formatList(l)
        self.assertEqual(len(l),3)
        self.assertEqual(l[0],self.template)
        self.assertEqual(l[2],self.template)
        
        #test template, entries,template
        p,e = TestHelper.createPlan(self,"TESE2T")

        l = p.step_list
        l = Plan.formatList(l)
        self.assertEqual(len(l),3)
        self.assertEqual(l[0],self.template)
        self.assertEqual(l[2],self.template)

    def test_changeByEntries(self):
        p,e = TestHelper.createPlan(self,"T")
        t = p.step_list
        entries = Plan.parseTextToEntries(load.loadData("material\\test\\test_update1.txt"))
        new_list = Plan.changeByEntries(t,entries)
        self.assertEqual(t[0],new_list[0])

    def test_doesEntryListContain(self):
        p,e = TestHelper.createPlan(self,"T")
        t = p.step_list
        entries = Plan.parseTextToEntries(load.loadData("material\\test\\test_update1.txt"))
        index = Plan.doesEntryListContain(t[0],entries)
        self.assertEqual(index,0)

    def test_update(self):
        #always the same template
        #test as p with 1 templates discover template
        p,e = TestHelper.createPlan(self,"T")
        p.update(load.loadData("material\\test\\test_update1.txt"))
        self.assertEqual(len(p.step_list),1)
        self.assertEqual(p.step_list[0].theme,self.template.theme)

        #test as p with 1 templates discover template+ entry
        p,e = TestHelper.createPlan(self,"T")
        p.update(load.loadData("material\\test\\test_update2.txt"))
        self.assertEqual(p.step_list[0].theme,self.template.theme)
        self.assertEqual(p.step_list[1].theme,"rofl")
        TestHelper.test_listByInstance(self,p.step_list,"2TE")

        #test as p with 2 templates discover 2 templates and 3 entries
        p,e = TestHelper.createPlan(self,"TT")
        p.update(load.loadData("material\\test\\test_update3.txt"))
        TestHelper.test_listByInstance(self,p.step_list,"5ETETE")
    



if __name__ == '__main__': 
    unittest.main()