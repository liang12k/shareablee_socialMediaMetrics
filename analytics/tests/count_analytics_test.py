import unittest
import datetime
from shareablee_socialMediaMetrics.analytics import count_analytics
from shareablee_socialMediaMetrics.dataextractors.mediadata_extractor import getMediaData

class Test_count_analytics(unittest.TestCase):
    def setUp(self):
        self.date_Jan01 = datetime.date(2014,1,1)
        self.date_Aug05 = datetime.date(2014,8,5)
        self.date_Sep05 = datetime.date(2014,9,5)
        self.class_UserCounts = count_analytics.UserCounts
        self.twitterData = getMediaData('twitter', "286200117457846272",
                                        self.date_Jan01, self.date_Aug05)
        self.googleplusData = getMediaData('googleplus', "100470681032489535736",
                                        self.date_Jan01, self.date_Aug05)

    def test_getAllData(self):
        # # what's the key for twitter's comment?
        self.class_UserCounts(self.twitterData, 'favorites_count', '', 'retweet_count', 'created_at')

    def test_getAllFavorites(self):
        # # what's the key for twitter's comment?
        self.class_UserCounts(self.twitterData, 'favorites_count', '', 'retweet_count', 'created_at')

    def test_getAllComments(self):
        # # what's the key for twitter's comment?
        self.class_UserCounts(self.twitterData, 'favorites_count', '', 'retweet_count', 'created_at')

    def test_getAllShares(self):
        # # what's the key for twitter's comment?
        self.class_UserCounts(self.twitterData, 'favorites_count', '', 'retweet_count', 'created_at')


if __name__ == '__main__':
    unittest.main()