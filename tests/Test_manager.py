import unittest
import sys
import os
join = os.path.join
sys.path.append(join('./production/logic'))
from plan import Plan 
from entry import Entry 

import ParseText
import re

class Test_Manager(unittest.TestCase):


    def test_insertTime(self):
        test_source = """00:01 hi wie gehts?

        00:03 mir gehts gut!
        """
        plan= Plan("heute")
        plan.add(Entry("00:02","hi wie gehts?",start="00:01"))
        plan.add(Entry("00:05","mir gehts gut!",start="00:03"))

        string = ParseText.insertTime( plan,test_source,1)  
        string = string.split("\n")

        t = test_source.split("\n")
        self.assertEqual(t[0],string[0])
        self.assertNotEqual(t[1],string[1])
        self.assertEqual(string[1],"00:03")
        self.assertEqual(t[2],string[2])



if __name__=="__main__":
    unittest.main()