import unittest
import datetime
from shareablee_socialMediaMetrics.analytics.googleplus_analytics import GoogleplusAnalytics
from shareablee_socialMediaMetrics.dataextractors.mediadata_extractor import getMediaData

class Test_GoogleplusAnalytics(unittest.TestCase):
    def setUp(self):
        self.date_Jan01 = datetime.date(2014,1,1)
        self.date_Aug05 = datetime.date(2014,8,5)
        self.date_Sep05 = datetime.date(2014,9,5)

        self.googleplusTestData()

    def googleplusTestData(self):
        self.googleplusData = getMediaData('googleplus', "100470681032489535736", self.date_Jan01, self.date_Aug05)
        self.googleplusobj_GoogleplusAnalytics = GoogleplusAnalytics(self.googleplusData,
                                                                    self.date_Jan01, self.date_Aug05)

    def test_getCountOfFavorites(self):
        self.assertEqual(1140, self.googleplusobj_GoogleplusAnalytics.getCountOfPlusones())

    def test_getCountOfReplies(self):
        self.assertEqual(96, self.googleplusobj_GoogleplusAnalytics.getCountOfComments())

    def test_getCountOfRetweets(self):
        self.assertEqual(88, self.googleplusobj_GoogleplusAnalytics.getCountOfReshares())

    def test_getCountOfTweets(self):
         self.assertEqual(3, self.googleplusobj_GoogleplusAnalytics.getCountOfPostnotes())

    def test_getCountOfActions(self):
        self.assertEqual({'total_actions': 1324}, self.googleplusobj_GoogleplusAnalytics.getCountOfActions())

    def test_getCountOfActionsPerTweet(self):
        self.assertEqual({'total_actions_per_post_note': 441},
                         self.googleplusobj_GoogleplusAnalytics.getCountOfActionsPerPostnote())


if __name__ == '__main__':
    unittest.main()