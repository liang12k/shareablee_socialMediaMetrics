import datetime
from shareablee_socialMediaMetrics.analytics.count_analytics import UserCounts

class GoogleplusAnalytics(UserCounts):
    """
    class handling getting the basic plusones, reshares, comments counts and metrics
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
        super(GoogleplusAnalytics, self).__init__(inpUserData, favoritesKeyStr, commentsKeyStr,
                                                  sharesKeyStr, dateKeyStr)
        self.startdate =    startDate
        self.enddate =      endDate

    def getCountOfPlusones(self):
        """
        :return: int count of plusones
        """
        return self.getCountOfAllFavorites(self.startdate, self.enddate)[0]

    def getCountOfComments(self):
        """
        :return: int count of comments
        """
        return self.getCountOfAllComments(self.startdate, self.enddate)[0]

    def getCountOfReshares(self):
        """
        :return: int count of reshares
        """
        return self.getCountOfAllShares(self.startdate, self.enddate)[0]

    def getCountOfPostnotes(self):
        """
        :return: int count of post notes
        """
        return self.getCountOfAllPostings(self.startdate, self.enddate,
                                          selectFieldsDict={'verb':lambda x: x.lower()=='post',
                                                            'object_type':lambda x: x.lower()=='note'})[0]

    def getCountOfActions(self):
        """
        :return: int sum of the counts of (plusones, reshares, comments)
        """
        countFuncs = [self.getCountOfPlusones, self.getCountOfReshares, self.getCountOfComments]
        return {'total_actions' : sum([f() for f in countFuncs])}

    def getCountOfActionsPerPostnote(self):
        """
        :return: int sum of the counts of (plusones, reshares, comments) per post note
        """
        try:
            totalActionsPerNote = self.getCountOfActions()['total_actions']/self.getCountOfPostnotes()
        except ZeroDivisionError:
            totalActionsPerNote = 0
        return {'total_actions_per_post_note' : totalActionsPerNote}