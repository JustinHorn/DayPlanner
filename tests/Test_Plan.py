import unittest
import sys
sys.path.append('.\\production\\logic')
import calcTime 
import load 
from entry import Entry 
from plan import Plan 

class Test_Plan(unittest.TestCase):

    test_source = "material\\test\\test_template_1.txt"

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = load.loadTemplate(Test_Plan.test_source)

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
        plan = self.get_x_template_plan(3)

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

    def test_planEqual(self):
        plan1 = Plan("1")
        plan2 = Plan("2")

        plan1.add(self.template)
        plan2.add(self.template)

        self.assertEqual(plan1,plan2)
        self.assertNotEqual(id(plan1),id(plan2))
    
    def get_x_template_plan(self,x:int):
        plan = Plan("today"):
        for i in range(x):
            plan.add(self.template)
        return plan
                    


        

        


if __name__ == '__main__': 
    unittest.main()