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

        # # in_reply_to_user_id ?= key for twitter's replies?
        self.twitterobj_UserCounts = UserCounts(self.twitterData,
                                               'favorite_count', 'in_reply_to_screen_name',
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
        gplusObj_allData = self.googleplusobj_UserCounts.getAllData
        twtObj_allData = self.twitterobj_UserCounts.getAllData
        self.assertTrue(isinstance(gplusObj_allData(self.date_Jan01, self.date_Aug05), dict))
        self.assertTrue(isinstance(gplusObj_allData(self.date_Jan01, self.date_Aug05,
                                                   self.gplusSelectFields), dict))
        self.assertTrue(isinstance(twtObj_allData(self.date_Jan01, self.date_Aug05), dict))
        self.assertTrue(isinstance(twtObj_allData(self.date_Jan01, self.date_Aug05,
                                                self.twtrSelectFields), dict))

    def test_getAllFavorites(self):
        gplusObj_allFavorites = self.googleplusobj_UserCounts.getCountOfAllFavorites
        twtObj_allFavorites = self.twitterobj_UserCounts.getCountOfAllFavorites
        self.assertTrue(isinstance(gplusObj_allFavorites(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(gplusObj_allFavorites(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(gplusObj_allFavorites(self.date_Jan01, self.date_Aug05,
                                                           self.gplusSelectFields), tuple))
        self.assertTrue(isinstance(twtObj_allFavorites(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(twtObj_allFavorites(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(twtObj_allFavorites(self.date_Jan01, self.date_Aug05,
                                                        self.twtrSelectFields), tuple))

    def test_zerocount_getAllFavorites(self):
        # # out of date range of dataset
        gplusObj_allFavorites = self.googleplusobj_UserCounts.getCountOfAllFavorites
        twtObj_allFavorites = self.twitterobj_UserCounts.getCountOfAllFavorites
        self.assertTrue(isinstance(gplusObj_allFavorites(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(gplusObj_allFavorites(self.date_Aug05, self.date_Sep05)[0], 0)
        self.assertTrue(isinstance(twtObj_allFavorites(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(twtObj_allFavorites(self.date_Aug05, self.date_Sep05)[0], 0)

    def test_getAllComments(self):
        gplusObj_allComments = self.googleplusobj_UserCounts.getCountOfAllComments
        twtObj_allComments = self.twitterobj_UserCounts.getCountOfAllComments
        self.assertTrue(isinstance(gplusObj_allComments(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(gplusObj_allComments(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(gplusObj_allComments(self.date_Jan01, self.date_Aug05,
                                                        self.gplusSelectFields), tuple))
        self.assertTrue(isinstance(twtObj_allComments(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(twtObj_allComments(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(twtObj_allComments(self.date_Jan01, self.date_Aug05,
                                                    self.twtrSelectFields), tuple))

    def test_zerocount_getAllComments(self):
        # # out of date range of dataset
        gplusObj_allComments = self.googleplusobj_UserCounts.getCountOfAllComments
        twtObj_allComments = self.twitterobj_UserCounts.getCountOfAllComments
        self.assertTrue(isinstance(gplusObj_allComments(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(gplusObj_allComments(self.date_Aug05, self.date_Sep05)[0], 0)
        self.assertTrue(isinstance(twtObj_allComments(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(twtObj_allComments(self.date_Aug05, self.date_Sep05)[0], 0)

    def test_getAllShares(self):
        gplusObj_allShares = self.googleplusobj_UserCounts.getCountOfAllShares
        twtObj_allShares = self.twitterobj_UserCounts.getCountOfAllShares
        self.assertTrue(isinstance(gplusObj_allShares(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(gplusObj_allShares(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(gplusObj_allShares(self.date_Jan01, self.date_Aug05,
                                                    self.gplusSelectFields), tuple))
        self.assertTrue(isinstance(twtObj_allShares(self.date_Jan01, self.date_Aug05), tuple))
        self.assertTrue(isinstance(twtObj_allShares(self.date_Jan01, self.date_Aug05)[0], int))
        self.assertTrue(isinstance(twtObj_allShares(self.date_Jan01, self.date_Aug05,
                                                    self.twtrSelectFields), tuple))

    def test_zerocount_getAllShares(self):
        # # out of date range of dataset
        gplusObj_allShares = self.googleplusobj_UserCounts.getCountOfAllShares
        twtObj_allShares = self.twitterobj_UserCounts.getCountOfAllShares
        self.assertTrue(isinstance(gplusObj_allShares(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(gplusObj_allShares(self.date_Aug05, self.date_Sep05)[0], 0)
        self.assertTrue(isinstance(twtObj_allShares(self.date_Aug05, self.date_Sep05), tuple))
        self.assertEqual(twtObj_allShares(self.date_Aug05, self.date_Sep05)[0], 0)


if __name__ == '__main__':
    unittest.main()