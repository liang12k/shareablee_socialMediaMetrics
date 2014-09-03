import glob
import unittest

def runTests_inTestDirectory():
    """
    method to be imported and used in test directories to run unittests
    leveraged from:
    http://stackoverflow.com/questions/1732438/run-all-unit-test-in-python-directory/24562019#24562019
    """
    test_file_strings = glob.glob('*_test.py')
    module_strings = [str[0:len(str)-3] for str in test_file_strings]
    suites = [unittest.defaultTestLoader.loadTestsFromName(str) for str
              in module_strings]
    testSuite = unittest.TestSuite(suites)
    text_runner = unittest.TextTestRunner().run(testSuite)