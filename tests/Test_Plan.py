import unittest
import sys
sys.path.append('.\\production\\logic')
import calcTime 
import load 
from entry import Entry 
from plan import Plan 
from template import Template

class Test_Plan(unittest.TestCase):

    test_source = "material\\test\\test_template_1.txt"

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = load.loadTemplate(Test_Plan.test_source)

    def test_addToPlan(self):
        entry1 = Entry("03:00","Talking")
        entry2 = Entry("02:00","Sport")
        p = Plan("today")
        p.add(entry1)
        p.add(entry2)
        self.assertEqual(p.step_list[0].start,"07:00")
        self.assertEqual(p.step_list[1].start,"10:00")

    def test_addToPlan_2(self):
        entry1 = Entry("03:00","Talking")
        entry2 = Entry("02:00","Sport")
        p = Plan("today")
        p.add(entry1)
        p.add(self.template)
        p.add(entry2)

        step_list = p.step_list
        self.assertEqual(step_list[0].start,Plan.STANDARD_START)
        self.assertEqual(step_list[1].start,calcTime.addTime(Plan.STANDARD_START,step_list[0].duration))
        self.assertEqual(step_list[2].start,calcTime.addTime(step_list[1].start,step_list[1].duration))
    
    def test_removeElement(self):
        p = self.get_x_template_p(3)

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
    
    def get_x_template_p(self,x:int):
        p = Plan("today")
        for i in range(x):
            p.add(self.template)
        return p

    def createPlan(string:str):
        # eEEET2E3 - needs to be done some other time!

        
        pass 


    def test_entriesToTemplate(self):
        #test only entries
        p = Plan("hello")
        e = Entry("03:00","this shit gets cloned")
        p.add(e)
        p.add(Entry("03:00","Talking"))
        p.add(Entry("03:00","Talking"))
        l = p.step_list
        l = Plan.formatList(l)
        self.assertEqual(len(l),1)
        self.assertEqual(len(l[0].step_list),3)
        self.assertEqual(l[0].step_list[0],e)


        #test entrie,template,entrie
        p = Plan("hello")
        e = Entry("03:00","this shit gets cloned")
        p.add(e)
        p.add(self.template)
        p.add(Entry("03:00","Talking"))
        l = p.step_list
        l = Plan.formatList(l)
        self.assertEqual(len(l),3)
        self.assertEqual(l[1],self.template)
        self.assertEqual(l[0],e)

        #test entries,template,entries
        p = Plan("hello")
        e = Entry("03:00","this shit gets cloned")
        p.add(e)
        p.add(Entry("03:00","Talking"))
        p.add(self.template)
        p.add(Entry("03:00","Talking"))
        p.add(Entry("03:00","Talking"))

        l = p.step_list
        l = Plan.formatList(l)
        self.assertEqual(len(l[2].step_list),2)
        self.assertEqual(l[1],self.template)
        self.assertEqual(l[0].step_list[0],e)

        #test template,entrie,template
        p = Plan("hello")
        e = Entry("03:00","this shit gets cloned")
        p.add(self.template)
        p.add(e)
        p.add(self.template)

        l = p.step_list
        l = Plan.formatList(l)
        self.assertEqual(len(l),3)
        self.assertEqual(l[0],self.template)
        self.assertEqual(l[2],self.template)
        
        #test template, entries,template
        p = Plan("hello")
        e = Entry("03:00","this shit gets cloned")
        p.add(self.template)
        p.add(e)
        p.add(Entry("03:00","Talking"))
        p.add(Entry("03:00","Talking"))
        p.add(self.template)

        l = p.step_list
        l = Plan.formatList(l)
        self.assertEqual(len(l),3)
        self.assertEqual(l[0],self.template)
        self.assertEqual(l[2],self.template)

    def test_changeByEntries(self):
        p = self.get_x_template_p(1)
        t = p.step_list
        entries = Plan.parseTextToEntries(load.loadData("material\\test\\test_update1.txt"))
        new_list = Plan.changeByEntries(t,entries)
        self.assertEqual(t[0],new_list[0])
        pass

    def test_doesEntryListContain(self):
        p = self.get_x_template_p(1)
        t = p.step_list
        entries = Plan.parseTextToEntries(load.loadData("material\\test\\test_update1.txt"))
        index = Plan.doesEntryListContain(t[0],entries)
        self.assertEqual(index,0)

    def test_update(self):
        #always the same template
        #test as p with 1 templates discover template
        p = self.get_x_template_p(1)
        p.update(load.loadData("material\\test\\test_update1.txt"))
        self.assertEqual(len(p.step_list),1)
        self.assertEqual(p.step_list[0].theme,self.template.theme)

        #test as p with 1 templates discover template+ entry
        p = self.get_x_template_p(1)
        p.update(load.loadData("material\\test\\test_update2.txt"))
        self.assertEqual(len(p.step_list),2)
        self.assertEqual(p.step_list[0].theme,self.template.theme)
        self.assertEqual(p.step_list[1].theme," rofl")

        #test as p with 2 templates discover 2 templates and 3 entries
        p = self.get_x_template_p(2)
        p.update(load.loadData("material\\test\\test_update3.txt"))
        self.assertTrue(len(p.step_list),5)
        self.assertTrue(isinstance(p.step_list[0],Entry))
        self.assertTrue(isinstance(p.step_list[1],Template))
        self.assertTrue(isinstance(p.step_list[2],Entry))
        self.assertTrue(isinstance(p.step_list[3],Template))
        self.assertTrue(isinstance(p.step_list[4],Entry))
        pass



        

        


if __name__ == '__main__': 
    unittest.main()