import unittest
import datetime
from shareablee_socialMediaMetrics.utils import dateconversions

class Test_dateconversions(unittest.TestCase):
    def test_convertTwitterDate(self):
        self.assertEqual(datetime.date(2014,10,22),
                        dateconversions.convertTwitterDate("2014-10-22T00:00:00").date())
        self.assertEqual(datetime.date(2014,3,1),
                        dateconversions.convertTwitterDate("2014-03-01T00:00:00").date())
        self.assertEqual(datetime.date(2014,11,25),
                        dateconversions.convertGoogleplusDate(datetime.datetime(2014,11,25)).date())
        self.assertEqual(datetime.date(2014,4,1),
                        dateconversions.convertGoogleplusDate(datetime.datetime(2014,4,1)).date())


if __name__ == '__main__':
    unittest.main()