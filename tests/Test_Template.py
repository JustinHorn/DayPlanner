import unittest
import sys
sys.path.append('.\\production\\')
import calcTime
import load
from entry import Entry
from plan import Plan

class Test_Template(unittest.TestCase):

    test_source = "material\\test\\test_template_1.txt"

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = load.loadTemplate(Test_Template.test_source)
      
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

    def test_splitTempalte(self):
        sl0 = self.template.step_list

        split_point =int(len(sl0)/2)
        template1,template2 = self.template.split(split_point)
        
        sl1 = template1.step_list
        sl2 = template2.step_list

        l1 = len(sl1)
        l2 = len(sl2)

        self.assertEqual(l1+l2,len(sl0))
        
        for i,e in enumerate(sl1):
            self.assertEqual(e.theme,sl0[i].theme)
            self.assertEqual(e.duration,sl0[i].duration)
            self.assertNotEqual(e,sl0[i])
    
        for i,e in enumerate(sl2):
            self.assertEqual(e.theme,sl0[i+l1].theme)
            self.assertEqual(e.duration,sl0[i+l1].duration)
            self.assertNotEqual(e,sl0[i+l1])







if __name__ == '__main__': 
    unittest.main()