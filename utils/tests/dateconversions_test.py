import unittest
import datetime
from shareablee_socialMediaMetrics.utils.dateconversions import convertTwitterDate

class Test_dateconversions(unittest.TestCase):
    def test_convertTwitterDate(self):
        self.assertEqual(datetime.date(2014,10,22),
                        convertTwitterDate("2014-10-22T00:00:00"))
        self.assertEqual(datetime.date(2014,3,1),
                        convertTwitterDate("2014-03-01T00:00:00"))


if __name__ == '__main__':
    unittest.main()