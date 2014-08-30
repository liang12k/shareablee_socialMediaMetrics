import unittest
import datetime
from shareablee_socialMediaMetrics.dataextractors.mediadata_extractor import getMediaData
from shareablee_socialMediaMetrics.datastore import twitter_mockdata, googleplus_mockdata

class Test_getMediaData(unittest.TestCase):
    def setUp(self):
        self.user_id_twitter =      "286200117457846272"
        self.user_id_googleplus =   "100470681032489535736"
        self.date_Jan01 = datetime.date(2014,1,1)
        self.date_Aug05 = datetime.date(2014,8,5)

    def test_keyerror_getMediaData(self):
        self.assertRaises(KeyError, getMediaData,
                          'miscMedia', self.user_id_twitter,
                          self.date_Jan01, self.date_Aug05)

    def test_twitter_getMediaData(self):
        self.assertEquals([twitter_mockdata.status2],
                          getMediaData('twitter', self.user_id_twitter,
                                        self.date_Jan01, self.date_Aug05))

    def test_googleplus_getMediaData(self):
        self.assertEquals([googleplus_mockdata.activity0, googleplus_mockdata.activity1,
                           googleplus_mockdata.activity2, googleplus_mockdata.activity3],
                          getMediaData('googleplus', self.user_id_googleplus,
                                        self.date_Jan01, self.date_Aug05))


if __name__ == '__main__':
    unittest.main()