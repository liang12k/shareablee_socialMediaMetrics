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
        self.twtrSelectFields = {'retweeted_status':None, 'in_reply_to_user_id':None, 'in_reply_to_status_id':None}
        self.twitterData = getMediaData('twitter', "286154818974646272",
                                        self.date_Jan01, self.date_Aug05)
        # # converting the date to datetime.date to run unittest; can't override '_getDateTypeFormat'
        for tData in self.twitterData:
            tData['created_at']= dateconversions.convertTwitterDate(tData['created_at'])

        # # what's the key for twitter's comment?
        self.twitterobj_UserCounts = UserCounts(self.twitterData,
                                               'favorite_count', '',
                                               'retweet_count', 'created_at')

    def googleplusTestData(self):
        self.gplusSelectFields = {'verb':'post', 'object_type':'note'}
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
        gplusObj = self.googleplusobj_UserCounts
        twtObj = self.twitterobj_UserCounts
        self.assertTrue(isinstance(gplusObj.getAllData(self.date_Jan01, self.date_Aug05), dict))
        self.assertTrue(isinstance(gplusObj.getAllData(self.date_Jan01, self.date_Aug05, self.gplusSelectFields), dict))
        self.assertTrue(isinstance(twtObj.getAllData(self.date_Jan01, self.date_Aug05), dict))
        self.assertTrue(isinstance(twtObj.getAllData(self.date_Jan01, self.date_Aug05, self.twtrSelectFields), dict))

    def test_getAllFavorites(self):
        gplusObj = self.googleplusobj_UserCounts
        twtObj = self.twitterobj_UserCounts
        self.assertTrue(isinstance(gplusObj.getAllFavorites(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(gplusObj.getAllFavorites(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(gplusObj.getAllFavorites(self.date_Jan01, self.date_Aug05,
                                                            self.gplusSelectFields), tuple))
        self.assertTrue(isinstance(twtObj.getAllFavorites(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(twtObj.getAllFavorites(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(twtObj.getAllFavorites(self.date_Jan01, self.date_Aug05,
                                                          self.twtrSelectFields), tuple))

    def test_zerocount_getAllFavorites(self):
        # # out of daterange of dataset
        gplusObj = self.googleplusobj_UserCounts
        twtObj = self.twitterobj_UserCounts
        self.assertTrue(isinstance(gplusObj.getAllFavorites(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(gplusObj.getAllFavorites(self.date_Aug05, self.date_Sep05)[0], 0)
        self.assertTrue(isinstance(twtObj.getAllFavorites(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(twtObj.getAllFavorites(self.date_Aug05, self.date_Sep05)[0], 0)

    def test_getAllComments(self):
        gplusObj = self.googleplusobj_UserCounts
        twtObj = self.twitterobj_UserCounts
        self.assertTrue(isinstance(gplusObj.getAllComments(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(gplusObj.getAllComments(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(gplusObj.getAllComments(self.date_Jan01, self.date_Aug05,
                                                           self.gplusSelectFields), tuple))
        self.assertTrue(isinstance(twtObj.getAllComments(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(twtObj.getAllComments(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(twtObj.getAllComments(self.date_Jan01, self.date_Aug05,
                                                         self.twtrSelectFields), tuple))

    def test_zerocount_getAllComments(self):
        # # out of daterange of dataset
        gplusObj = self.googleplusobj_UserCounts
        twtObj = self.twitterobj_UserCounts
        self.assertTrue(isinstance(gplusObj.getAllComments(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(gplusObj.getAllComments(self.date_Aug05, self.date_Sep05)[0], 0)
        self.assertTrue(isinstance(twtObj.getAllComments(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(twtObj.getAllComments(self.date_Aug05, self.date_Sep05)[0], 0)

    def test_getAllShares(self):
        gplusObj = self.googleplusobj_UserCounts
        twtObj = self.twitterobj_UserCounts
        self.assertTrue(isinstance(gplusObj.getAllShares(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(gplusObj.getAllShares(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(gplusObj.getAllShares(self.date_Jan01, self.date_Aug05,
                                                         self.gplusSelectFields), tuple))
        self.assertTrue(isinstance(twtObj.getAllShares(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(twtObj.getAllShares(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(twtObj.getAllShares(self.date_Jan01, self.date_Aug05,
                                                       self.twtrSelectFields), tuple))

    def test_zerocount_getAllShares(self):
        # # out of daterange of dataset
        gplusObj = self.googleplusobj_UserCounts
        twtObj = self.twitterobj_UserCounts
        self.assertTrue(isinstance(gplusObj.getAllShares(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(gplusObj.getAllShares(self.date_Aug05, self.date_Sep05)[0], 0)
        self.assertTrue(isinstance(twtObj.getAllShares(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(twtObj.getAllShares(self.date_Aug05, self.date_Sep05)[0], 0)


if __name__ == '__main__':
    unittest.main()