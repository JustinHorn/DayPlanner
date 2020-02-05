import unittest
import sys
import os
sys.path.append(os.path.join('./production/logic'))
import load


class Test_Load(unittest.TestCase):

    test_source = "material/test/"

    def Load(self):
        load.loadTemplateDir(self.test_source)


if __name__ == '__main__':
    unittest.main()
