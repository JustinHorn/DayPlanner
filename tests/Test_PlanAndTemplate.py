import unittest
import sys
sys.path.append('.\\production\\')
import calcTime
import load
from entry import Entry
from plan import Plan

class Test_PlansAndTemplates(unittest.TestCase):

    test_source = "material\\test\\test_template_1.txt"

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = load.loadTemplate(Test_PlansAndTemplates.test_source)

    def test_parseData(self):
        step_list = self.template.step_list
        self.assertEqual(step_list[0].duration ,"00:03")
        self.assertEqual(step_list[1].duration , "00:05")
        self.assertEqual(step_list[2].duration , "00:03")
        self.assertEqual(step_list[3].duration , "00:04")
        self.assertEqual(step_list[4].duration , "00:05")
        self.assertEqual(step_list[5].duration , "00:20")
        self.assertEqual(step_list[0].theme , "Aufstehen, Bett machen, ins Bad, ausziehen, in die Dusche gehen")

    def test_addTemplateToPlan(self):
        plan = Plan("today")
        plan.add(self.template)

    def test_addToPlan(self):
        entry1 = Entry("03:00","Talking")
        entry2 = Entry("02:00","Sport")
        plan = Plan("today")
        plan.add(entry1)
        plan.add(entry2)
        self.assertEqual(plan.step_list[0].start,"07:00")
        self.assertEqual(plan.step_list[1].start,"10:00")

    def test_addToPlan_2(self):
        entry1 = Entry("03:00","Talking")
        entry2 = Entry("02:00","Sport")
        plan = Plan("today")
        plan.add(entry1)
        plan.add(self.template)
        plan.add(entry2)
        step_list = plan.step_list
        self.assertEqual(step_list[0].start,Plan.STANDARD_START)
        self.assertEqual(step_list[1].start,calcTime.addTime(Plan.STANDARD_START,step_list[0].duration))
        self.assertEqual(step_list[2].start,calcTime.addTime(step_list[1].start,step_list[1].duration))

    def test_getText(self):
        plan = Plan("Today")
        plan.add(self.template)
        print(plan.getText())
    
    def test_removeElement(self):
        plan = Plan("Today")
        plan.add(self.template)
        plan.add(self.template)
        plan.add(self.template)
        self.assertNotEqual(Plan.STANDARD_START,plan.step_list[1].start)
        self.assertEqual(3,len(plan.step_list))
        end = plan.end

        plan.remove(0)
        self.assertEqual(Plan.STANDARD_START,plan.step_list[0].start)
        self.assertEqual(2,len(plan.step_list))
        self.assertNotEqual(end,plan.end)

    def test_removeElement(self):
        t1 = self.template.clone()
        t2 = self.template.clone()
 
        plan = Plan("Today")
        plan.add(t1)
        plan.add(self.template)
        plan.add(t2)
        
        endBefore = plan.end
        plan.splitTemplate(1,2)

        self.assertEqual(endBefore,plan.end)
        self.assertEqual(len(plan.step_list),4)
        self.assertEqual(plan.step_list[0].theme,t1.theme)
        self.assertEqual(plan.step_list[3].theme,t2.theme)



        


if __name__ == '__main__': 
    unittest.main()