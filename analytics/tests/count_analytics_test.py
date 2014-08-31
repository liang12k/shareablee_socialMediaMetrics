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

        self.twitterData = self.twitterTestData()
        # # what's the key for twitter's comment?
        self.twitterobj_UserCounts = UserCounts(self.twitterData,
                                               'favorites_count', '',
                                               'retweet_count', 'created_at')

        self.googleplusData = self.googleplusTestData()
        self.googleplusobj_UserCounts = UserCounts(self.googleplusData,
                                                   'plusones_count', 'comments_count',
                                                   'reshares_count', 'updated')

    def twitterTestData(self):
        twitterData = getMediaData('twitter', "286200117457846272",
                                    self.date_Jan01, self.date_Aug05)
        # # converting the date to datetime.date to run unittest; can't override '_getDateTypeFormat'
        for tData in twitterData:
            tData['created_at']= dateconversions.convertTwitterDate(tData['created_at'])

    def googleplusTestData(self):
        googlplusData = getMediaData('googleplus', "100470681032489535736",
                                    self.date_Jan01, self.date_Aug05)
        # # converting the date to datetime.date to run unittest; can't override '_getDateTypeFormat'
        for gpData in googlplusData:
            googlplusData['updated']=googlplusData['updated'].date()

    def test_getAllData(self):
        return

    def test_getAllFavorites(self):
        return

    def test_getAllComments(self):
        return

    def test_getAllShares(self):
        return


if __name__ == '__main__':
    unittest.main()