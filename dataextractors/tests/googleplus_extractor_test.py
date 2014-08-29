import unittest
import datetime
from shareablee_socialMediaMetrics.dataextractors.googleplus_extractor import getGooglePlus_userData
from shareablee_socialMediaMetrics.datastore import googleplus_mockdata

class Test_getGooglePlus_userData(unittest.TestCase):
    def setUp(self):
        self.user_id_activity0 = googleplus_mockdata.activity0
        self.date_Jul14 = datetime.date(2014,7,14)
        self.date_Jul19 = datetime.date(2014,7,19)
        self.date_Jul25 = datetime.date(2014,7,25)

    def test_nonuserid_getGooglePlus_userData(self):
        # # invalid user_id
        self.assertEqual([ ], getGooglePlus_userData('012012012012012012',
                                                    self.date_Jul14, self.date_Jul19))

    def test_validuserid_getGooglePlus_userData(self):
        # # valid user_id, gets the activity0 of mock data
        self.assertEqual([self.user_id_activity0], getGooglePlus_userData('100470681032489535736',
                                                                        self.date_Jul14,
                                                                        self.date_Jul14))

    def test_notindaterange_getGooglePlus_userData(self):
        # # valid user_id, but beyond the start/end date range
        self.assertEqual([ ], getGooglePlus_userData('100470681032489535736',
                                                    self.date_Jul19, self.date_Jul25))


if __name__ == '__main__':
    unittest.main()