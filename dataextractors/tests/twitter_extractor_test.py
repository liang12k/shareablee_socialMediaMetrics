#!/usr/bin/env python

import unittest
import datetime
from shareablee_socialMediaMetrics.dataextractors.twitter_extractor import getTwitter_userData
from shareablee_socialMediaMetrics.datastore import twitter_mockdata
# from ..twitter_extractor import getTwitter_userData
# from ...datastore import twitter_mockdata


class Test_getTwitter_userData(unittest.TestCase):
    def setUp(self):
        self.user_id_status0 = twitter_mockdata.status0
        self.date_Jan01 = datetime.datetime(2014,1,1)
        self.date_Jan05 = datetime.datetime(2014,1,5)
        self.date_Jan09 = datetime.datetime(2014,1,9)
    
    def test_nonuserid_getTwitter_userData(self):
        # # invalid user_id
        self.assertEqual([ ], getTwitter_userData('012012012012012012',
                                                self.date_Jan01, self.date_Jan05))
    
    def test_validuserid_getTwitter_userData(self):
        # # valid user_id, gets the status0 of mock data
        self.assertEqual([self.user_id_status0], getTwitter_userData('286154818974646272',
                                                                    self.date_Jan01,
                                                                    self.date_Jan05))

    def test_notindaterange_getTwitter_userData(self):
        # # valid user_id, but beyond the start/end date range
        self.assertEqual([ ], getTwitter_userData('286154818974646272',
                                                self.date_Jan05, self.date_Jan09))


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test_getTwitter_userData)
    # unittest.TextTestRunner().run(suite)
