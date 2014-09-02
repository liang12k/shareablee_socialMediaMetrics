import datetime
from shareablee_socialMediaMetrics.analytics.count_analytics import UserCounts

class TwitterAnalytics(UserCounts):
    """
    class handling getting the basic favorites, retweets, replies counts and metrics
    """

    def __init__(self, inpUserData=[], favoritesKeyStr='', commentsKeyStr='', sharesKeyStr='', dateKeyStr='',
                startDate=None, endDate=None):
        super(TwitterAnalytics, self).__init__()
        self.startdate = startDate
        self.enddate = endDate

    def getCountOfFavorites(self, selectFieldsDict={}):
        return self.getCountOfAllFavorites(self.startdate, self.enddate, selectFieldsDict={})

    def getCountOfReplies(self, selectFieldsDict={}):
        return self.getCountOfAllComments(self.startdate, self.enddate, selectFieldsDict={})

    def getCountOfRetweets(self, selectFieldsDict={}):
        return self.getCountOfAllShares(self.startdate, self.enddate, selectFieldsDict={})

    def getCountOfTweets(self, selectFieldsDict={}):
        return self.getCountOfAllActions(self.startdate, self.enddate, selectFieldsDict={})

    def getCountOfActions(self, selectFieldsDict={}):
        return self.getCountOfAllActions(self.startdate, self.enddate, selectFieldsDict={})