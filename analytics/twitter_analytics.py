import datetime
from shareablee_socialMediaMetrics.analytics.count_analytics import UserCounts

class TwitterAnalytics(UserCounts):
    """
    class handling getting the basic favorites, retweets, replies counts and metrics
    """
    def __init__(self, inpUserData=[], favoritesKeyStr='', commentsKeyStr='', sharesKeyStr='', dateKeyStr='',
                startDate=None, endDate=None):
        """
        :param inpUserData: list of dicts (user's dicts of social media info)
        :param favoritesKeyStr: dict string key representing user's favorites in dicts
        :param commentsKeyStr: dict string key representing user's comments in dicts
        :param sharesKeyStr: dict string key representing user's shares in dicts
        :param dateKeyStr: dict string key representing date in user's dicts
        :type startDate: datetime.date
        :type endDate: datetime.date
        """
        super(TwitterAnalytics, self).__init__(inpUserData, favoritesKeyStr, commentsKeyStr, sharesKeyStr, dateKeyStr)
        self.startdate =    startDate
        self.enddate =      endDate

    def getCountOfFavorites(self):
        """
        :return: int count of favorites
        """
        return self.getCountOfAllFavorites(self.startdate, self.enddate)[0]

    def getCountOfReplies(self):
        """
        :return: int count of replies
        """
        return self.getCountOfAllComments(self.startdate, self.enddate,
                                          selectFieldsDict={'in_reply_to_screen_name':'str'})[0]

    def getCountOfRetweets(self):
        """
        :return: int count of retweets
        """
        return self.getCountOfAllShares(self.startdate, self.enddate)[0]

    def getCountOfTweets(self):
        """
        :return: int count of tweets
        """
        return self.getCountOfAllPostings(self.startdate, self.enddate,
                                          selectFieldsDict={'retweeted_status':None,
                                                            'in_reply_to_user_id':None,
                                                            'in_reply_to_status_id':None})[0]

    def getCountOfActions(self):
        """
        :return: int sum of the counts of (favorites, shares, comments)
        """
        # return self.getCountOfAllActions(self.startdate, self.enddate)
        countFuncs = [self.getCountOfFavorites, self.getCountOfRetweets, self.getCountOfReplies]
        return {'total_actions' : sum([f() for f in countFuncs])}

    def getCountOfActionsPerTweet(self):
        """
        :return: int sum of the counts of (favorites, shares, comments) per tweet
        """
        # return self.getCountOfAllActions(self.startdate, self.enddate)
        countFuncs = [self.getCountOfFavorites, self.getCountOfRetweets, self.getCountOfReplies]
        try:
            totalActionsPerTweet = sum([f() for f in countFuncs])/self.getCountOfTweets()
        except ZeroDivisionError:
            totalActionsPerTweet = 0
        return {'total_actions_per_tweet' : totalActionsPerTweet}