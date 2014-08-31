import unittest
import datetime
from shareablee_socialMediaMetrics.analytics.count_analytics import UserCounts
from shareablee_socialMediaMetrics.dataextractors.mediadata_extractor import getMediaData
from shareablee_socialMediaMetrics.utils import dateconversions

class Test_count_analytics(unittest.TestCase):
    def setUp(self):
        self.date_Jan01 = datetime.date(2014,1,1)
        self.date_Aug05 = datetime.date(2014,8,5)
        self.date_Sep05 = datetime.date(2014,9,5)

        self.twitterTestData()
        self.googleplusTestData()

    def twitterTestData(self):
        self.twitterData = getMediaData('twitter', "286200117457846272",
                                        self.date_Jan01, self.date_Aug05)
        # # converting the date to datetime.date to run unittest; can't override '_getDateTypeFormat'
        for tData in self.twitterData:
            tData['created_at']= dateconversions.convertTwitterDate(tData['created_at'])

        # # what's the key for twitter's comment?
        self.twitterobj_UserCounts = UserCounts(self.twitterData,
                                               'favorite_count', '',
                                               'retweet_count', 'created_at')

    def googleplusTestData(self):
        self.googleplusData = getMediaData('googleplus', "100470681032489535736",
                                            self.date_Jan01, self.date_Aug05)
        # # converting the date to datetime.date to run unittest; can't override '_getDateTypeFormat'
        for gpData in self.googleplusData:
            gpData['updated']=dateconversions.convertGoogleplusDate(gpData['updated'])

        self.googleplusobj_UserCounts = UserCounts(self.googleplusData,
                                                   'plusones_count', 'comments_count',
                                                   'reshares_count', 'updated')

    # def test_misc(self):
    #     self.assertEqual(True,False)

    def test_getAllData(self):
        self.assertTrue(isinstance(self.googleplusobj_UserCounts.getAllData(self.date_Jan01, self.date_Aug05), dict))
        self.assertTrue(isinstance(self.twitterobj_UserCounts.getAllData(self.date_Jan01, self.date_Aug05), dict))

    def test_getAllFavorites(self):
        gplusObj = self.googleplusobj_UserCounts
        twtObj = self.twitterobj_UserCounts
        self.assertTrue(isinstance(self.googleplusobj_UserCounts.getAllFavorites(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(self.googleplusobj_UserCounts.getAllFavorites(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(self.twitterobj_UserCounts.getAllFavorites(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(self.twitterobj_UserCounts.getAllFavorites(self.date_Jan01, self.date_Aug05)[0], int))

    def test_getAllComments(self):
        gplusObj = self.googleplusobj_UserCounts
        twtObj = self.twitterobj_UserCounts
        self.assertTrue(isinstance(self.googleplusobj_UserCounts.getAllComments(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(self.googleplusobj_UserCounts.getAllComments(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(self.twitterobj_UserCounts.getAllComments(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(self.twitterobj_UserCounts.getAllComments(self.date_Jan01, self.date_Aug05)[0], int))

    def test_getAllShares(self):
        gplusObj = self.googleplusobj_UserCounts
        twtObj = self.twitterobj_UserCounts
        self.assertTrue(isinstance(self.googleplusobj_UserCounts.getAllShares(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(self.googleplusobj_UserCounts.getAllShares(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(self.twitterobj_UserCounts.getAllShares(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(self.twitterobj_UserCounts.getAllShares(self.date_Jan01, self.date_Aug05)[0], int))


if __name__ == '__main__':
    unittest.main()