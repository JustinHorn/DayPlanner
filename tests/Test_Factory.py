import unittest
import sys
import os
sys.path.append(os.path.join('./production/logic'))
import CalcTime 
import load 
from entry import Entry 
from plan import Plan 
from template import Template
from Factory import parsePlanFromFileText
import TestHelper

class Test_Factory(unittest.TestCase):

    test_source = """14.02.2020 
Structure:
19:30 ... 2
20:15 ... 3
22:00 lege dich schlafen! 1
Content:
19:30 essen machen
20:00 Maily
20:15 snack
20:45 guck dir Excel an, rechne ein paar zahlen durch | baue einen Businessplan nach if then struktur!
21:30 plane den n�chsten Tag
22:00 lege dich schlafen!
"""

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.plan =    parsePlanFromFileText(self.test_source)


    def test_entryCount(self):
        self.assertEqual(len(self.plan.step_list),3)
    
    def test_startAndEnd(self):
        self.assertEqual(self.plan.start,"19:30")
        self.assertEqual(self.plan.end,"22:00")



    

if __name__ == '__main__': 
    unittest.main()