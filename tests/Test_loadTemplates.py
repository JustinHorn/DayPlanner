import unittest
import sys
sys.path.append('.\\production\\')
import logic.load


class Test_Load(unittest.TestCase):

    test_source = "material\\test\\"

    def load(self):
        load.loadTemplateDir(self.test_source)


if __name__ == '__main__':
    unittest.main()
