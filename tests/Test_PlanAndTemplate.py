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
        # entry1 = Entry("00:03","Aufstehen, Bett machen, ins Bad, ausziehen, in die Dusche gehen")
        # entry2 = Entry("00:05","Duschen")
        # entry3 = Entry("00.03","abtrocknen, Föhnen")
        # entry4 = Entry("00:04","Toilette")
        # entry5 = Entry("00:05","runter gehen, Wasser kochen, Maily kraueln, hochgehen")
        # entry6 = Entry("00:20","essen")


    def test_parseData(self):
        the_list = self.template.the_list
        self.assertEqual(the_list[0].duration ,"00:03")
        self.assertEqual(the_list[1].duration , "00:05")
        self.assertEqual(the_list[2].duration , "00:03")
        self.assertEqual(the_list[3].duration , "00:04")
        self.assertEqual(the_list[4].duration , "00:05")
        self.assertEqual(the_list[5].duration , "00:20")
        self.assertEqual(the_list[0].theme , "Aufstehen, Bett machen, ins Bad, ausziehen, in die Dusche gehen")

    # def test_renderPlan(self):
    #     plan = Plan()
    #     self.assertEquals(plan,self.hardcoded_Plan)

    def test_addTemplateToPlan(self):
        plan = Plan("today")
        plan.add(self.template)
        # self.assertEquals(plan,self.hardcoded_Plan_2)

    def test_addToPlan(self):
        entry1 = Entry("03:00","Talking")
        entry2 = Entry("02:00","Sport")
        plan = Plan("today")
        plan.add(entry1)
        plan.add(entry2)
        self.assertEqual(plan.the_list[0].start,"07:00")
        self.assertEqual(plan.the_list[1].start,"10:00")

    def test_addToPlan_2(self):
        entry1 = Entry("03:00","Talking")
        entry2 = Entry("02:00","Sport")
        plan = Plan("today")
        plan.add(entry1)
        plan.add(self.template)
        plan.add(entry2)
        the_list = plan.the_list
        self.assertEqual(the_list[0].start,Plan.STANDARD_START)
        self.assertEqual(the_list[1].start,calcTime.addTime(Plan.STANDARD_START,the_list[0].duration))
        self.assertEqual(the_list[2].start,calcTime.addTime(the_list[1].start,the_list[1].duration))

    def test_getText(self):
        plan = Plan("Today")
        plan.add(self.template)
        print(plan.getText())
    
    def test_removeElement(self):
        plan = Plan("Today")
        plan.add(self.template)
        plan.add(self.template)
        plan.add(self.template)
        self.assertNotEqual(Plan.STANDARD_START,plan.the_list[1].start)
        self.assertEqual(3,len(plan.the_list))
        end = plan.end

        plan.remove(0)
        self.assertEqual(Plan.STANDARD_START,plan.the_list[0].start)
        self.assertEqual(2,len(plan.the_list))
        self.assertNotEqual(end,plan.end)



    # def test_changeStartWork(self):
    #     plan = Plan(start="08:00",self.template)
    #     plan.changeStart("-00:30")
    #     p_the_list = plan.the_list
    #     t_the_list = plan.the_list[0].the_list
    #     self.assertEquals(p_the_list[0].start,"07:30")
    #     self.assertEquals(t_the_list[1].start,addTime(t_the_list[0].start,t_the_list[0].duration))
    #     plan.changeStart("01:00")
    #     self.assertEquals(p_the_list[0].start,"08:30")
    #     self.assertEquals(t_the_list[1].start,addTime(t_the_list[0].start,t_the_list[0].duration))

    # def test_doesEqualsWork(self):
    #     self.assertEquals(plan,plan)
    #     plan.add(template)
    #     self.assertEquals(plan, plan)
    #     plan2 = plan.clone().changeStart("00:05")
    #     self.assertFalse(plan,plane2)

    # def test_printPlan(self):
    #     print(self.hardcoded_Plan)    

if __name__ == '__main__': 
    unittest.main()