import datetime

# # TODO -- need to generalize the naming to handle numerous other media sources

class UserCounts(object):
    """
        class handles the counts of input list of dicts of social media datasets
        currently handling getting favorites, comments, shares.
        ex:
            twitter: favorites, retweets, replies
            googplus: plusone, reshares, comments
    """
    def __init__(self, inpUserData=[], favoritesKeyStr='', commentsKeyStr='', sharesKeyStr='', dateKeyStr=''):
        """
        :param inpUserData: list of dicts (user's dicts of social media info)
        :param favoritesKeyStr: dict string key representing user's favorites in dicts
        :param commentsKeyStr: dict string key representing user's comments in dicts
        :param sharesKeyStr: dict string key representing user's shares in dicts
        :param dateKeyStr: dict string key representing date in user's dicts
        """
        self.userdata = inpUserData
        self.favoriteskey = favoritesKeyStr
        self.commentskey = commentsKeyStr
        self.shareskey = sharesKeyStr
        self.datekey = dateKeyStr

    def getAllData(self, startDate, endDate):
        dataInDaterange = [datadict for datadict in self.userdata\
                                    if startDate <= self._getDateTypeFormat(datadict[self.datekey]) <= endDate]
        return self.collapseListOfDicts(dataInDaterange)

    def collapseListOfDicts(self, inpListOfUserDicts):
        """
        collapses a list of dicts into single dict

        :param inpListOfUserDicts: list of dicts
        :return: dict with all keys and tuple'ed values
        """
        outputDict = {}
        for dataDict in inpListOfUserDicts:
            for k in dataDict.keys():
                # # store all values as tuples; update with appending
                outputDict[k] = outputDict.get(k) + (dataDict[k]) if outputDict.get(k) else (dataDict[k])
                if k in [self.favoriteskey, self.commentskey, self.shareskey]:
                    # # store as sum of values for select keys
                    outputDict[k] = (sum([int(num) for num in outputDict[k]]))
        # # ref - http://stackoverflow.com/questions/16458340/python-equivalent-of-zip-for-dictionaries
        return outputDict

    def getAllFavorites(self, startDate, endDate):
        """
        :type startDate: datetime.date
        :type endDate: datetime.date
        :return: count of all the user's favorite content within date range
        """
        return self.getAllData(startDate, endDate).get(self.favoriteskey, 0)

    def getAllComments(self, startDate, endDate):
        """
        :type startDate: datetime.date
        :type endDate: datetime.date
        :return: count of all the user's comment content within date range
        """
        return self.getAllData(startDate, endDate)(self.commentskey, 0)

    def getAllShares(self, startDate, endDate):
        """
        :type startDate: datetime.date
        :type endDate: datetime.date
        :return: count of all the user's shares content within date range
        """
        return self.getAllData(startDate, endDate).get(self.shareskey, 0)

    def _getDateTypeFormat(self, inpDate):
        """
        override this method, convert date string to datetime.date

        :param inpDate: input date string format
        :return: datetime.date
        """
        return inpDate