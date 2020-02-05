import unittest
import sys
import os
join = os.path.join
sys.path.append(join('./production/logic'))
import load 
from plan import Plan 
from template import Template
import TestHelper
from formatStructure import FormatStructure
import ParseText

class Test_FormatStructure(unittest.TestCase):

    test_source = join("material/test/test_template_1.txt")

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template = load.loadTemplate(Test_FormatStructure.test_source)

    def test_formatList(self):
        p,e = TestHelper.createPlan(self,"ESE2")
        l = p.step_list
        l = FormatStructure(l).format()
        self.assertEqual(len(l[0].step_list),3)
        self.assertEqual(l[0].step_list[0],e)
        TestHelper.test_listByInstance(self,l,"1T")


    def test_formatList_2(self):
        #test entrie,template,entrie
        p,e = TestHelper.createPlan(self,"ESTE")
        l = p.step_list
        l = FormatStructure(l).format()
    
        self.assertEqual(l[0],e)
        TestHelper.test_listByInstance(self,l,"3ETE")


    def test_formatList_3(self):
        #test entries,template,entries
        p,e = TestHelper.createPlan(self,"ESETE2")
        l = p.step_list
        l = FormatStructure(l).format()
        self.assertEqual(len(l[2].step_list),2)
        self.assertEqual(l[0].step_list[0],e)
        TestHelper.test_listByInstance(self,l,"3TTT")


    def test_formatList_4(self):
        p,e = TestHelper.createPlan(self,"TEST")
        l = p.step_list
        l = FormatStructure(l).format()
        TestHelper.test_listByInstance(self,l,"3TET")

        
    def test_formatList_5(self):
        p,e = TestHelper.createPlan(self,"TESE2T")

        l = p.step_list
        l = FormatStructure(l).format()
        TestHelper.test_listByInstance(self,l,"3TTT")

if __name__=="__main__":
    unittest.main()