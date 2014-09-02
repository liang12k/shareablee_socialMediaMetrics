import unittest
import datetime
from shareablee_socialMediaMetrics.analytics.twitter_analytics import TwitterAnalytics
from shareablee_socialMediaMetrics.dataextractors.mediadata_extractor import getMediaData

class Test_TwitterAnalytics(unittest.TestCase):
    def setUp(self):
        self.date_Jan01 = datetime.date(2014,1,1)
        self.date_Aug05 = datetime.date(2014,8,5)
        self.date_Sep05 = datetime.date(2014,9,5)

        self.twitterTestData()
        self.googleplusTestData()

    def twitterTestData(self):
        self.twtrSelectFields = {'retweeted_status':None, 'in_reply_to_user_id':None, 'in_reply_to_status_id':None}
        self.twitterData = getMediaData('twitter', "286200117457846272", self.date_Jan01, self.date_Aug05)
        self.twitterobj_TwitterAnalytics = TwitterAnalytics(self.twitterData,
                                                            'favorite_count', 'in_reply_to_screen_name',
                                                            'retweet_count', 'created_at',
                                                            self.date_Jan01, self.date_Aug05)

    def googleplusTestData(self):
        self.gplusSelectFields = {'verb':'post', 'object_type':'note'}
        self.googleplusData = getMediaData('googleplus', "100470681032489535736", self.date_Jan01, self.date_Aug05)
        self.googleplusobj_TwitterAnalytics = TwitterAnalytics(self.googleplusData,
                                                            'plusones_count', 'comments_count',
                                                            'reshares_count', 'updated',
                                                            self.date_Jan01, self.date_Aug05)

    def test_getCountOfFavorites(self):
        self.assertEqual(600, self.twitterobj_TwitterAnalytics.getCountOfFavorites())

    def test_getCountOfReplies(self):
        self.assertEqual(1, self.twitterobj_TwitterAnalytics.getCountOfReplies())

    def test_getCountOfRetweets(self):
        self.assertEqual(700, self.twitterobj_TwitterAnalytics.getCountOfRetweets())

    def test_getCountOfTweets(self):
        # # user doesn't have a 'tweet', just a reply
         self.assertEqual(0, self.twitterobj_TwitterAnalytics.getCountOfTweets())

    def test_getCountOfActions(self):
        self.assertEqual({'total_actions': 1301}, self.twitterobj_TwitterAnalytics.getCountOfActions())

    def test_getCountOfActionsPerTweet(self):
        # # user doesn't have a 'tweet', just a reply
        self.assertEqual({'total_actions_per_tweet': 0}, self.twitterobj_TwitterAnalytics.getCountOfActionsPerTweet())


if __name__ == '__main__':
    unittest.main()