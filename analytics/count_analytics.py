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
        self.userdata =     inpUserData
        self.favoriteskey = favoritesKeyStr
        self.commentskey =  commentsKeyStr
        self.shareskey =    sharesKeyStr
        self.datekey =      dateKeyStr

    def getAllData(self, startDate, endDate, selectFieldsDict={}):
        """
        returns a collapsed dict of all values in tuples in respect
        to their key names
        3 fields - favoritesKeyStr, commentsKeyStr, sharesKeyStr are summed

        :type startDate: datetime.date
        :type endDate: datetime.date
        :param selectFieldsDict: dict used to filter the media data dicts to retrieve
                                 ex: dict {'verb':'post', 'object_type':'note'} for GooglePlus data
                                     will return dicts with those values present
        :rtype: dict
        """
        dataInDaterange = [datadict for datadict in self.userdata\
                                    if startDate <= datadict[self.datekey].date() <= endDate\
                                    and self._isInSelectDictFields(datadict, selectFieldsDict)]
        return self.collapseListOfDicts(dataInDaterange)

    def collapseListOfDicts(self, inpListOfUserDicts):
        """
        collapses a list of dicts into single dict

        :param inpListOfUserDicts: list of dicts
        :return: dict with all keys and tuple of values
        """
        outputDict = {}
        for dataDict in inpListOfUserDicts:
            for k in dataDict.keys():
                # # store all values as tuples; update with appending
                outputDict[k] = outputDict.get(k) + (dataDict[k],) if outputDict.get(k,()) else (dataDict[k],)
                if k in [self.favoriteskey, self.commentskey, self.shareskey]:
                    # countSum = 0
                    # for num in outputDict[k]:
                    #     if num:
                    #         countSum += 1 if isinstance(num, str) else num
                    # outputDict[k] = (countSum,)

                    # # store as sum of values for select keys
                    outputDict[k] = (sum([int(1 if isinstance(num, str) else 0) for num in outputDict[k] if num]),)
        # # can be taken as: ex: count of tweets, googleplus notes
        outputDict['dicts_with_selectfields_count'] = (len(inpListOfUserDicts),)
        return outputDict

    def getCountOfAllFavorites(self, startDate, endDate, selectFieldsDict={}):
        """
        :type startDate: datetime.date
        :type endDate: datetime.date
        :param selectFieldsDict: dict used to filter the media data dicts to retrieve
                                 ex: dict {'verb':'post', 'object_type':'note'} for GooglePlus data
                                     will return dicts with those values present
        :return: count of all the user's favorite content within date range
        """
        return self.getAllData(startDate, endDate, selectFieldsDict).get(self.favoriteskey, (0,))

    def getCountOfAllComments(self, startDate, endDate, selectFieldsDict={}):
        """
        :type startDate: datetime.date
        :type endDate: datetime.date
        :param selectFieldsDict: dict used to filter the media data dicts to retrieve
                                 ex: dict {'verb':'post', 'object_type':'note'} for GooglePlus data
                                     will return dicts with those values present
        :return: count of all the user's comment content within date range
        """
        return self.getAllData(startDate, endDate, selectFieldsDict).get(self.commentskey, (0,))

    def getCountOfAllShares(self, startDate, endDate, selectFieldsDict={}):
        """
        :type startDate: datetime.date
        :type endDate: datetime.date
        :param selectFieldsDict: dict used to filter the media data dicts to retrieve
                                 ex: dict {'verb':'post', 'object_type':'note'} for GooglePlus data
                                     will return dicts with those values present
        :return: count of all the user's shares content within date range
        """
        return self.getAllData(startDate, endDate, selectFieldsDict).get(self.shareskey, (0,))

    def getCountOfAllActions(self, startDate, endDate, selectFieldsDict={}):
        """
        returns int sum of the counts of favorites, shares, comments
        can be overridden to get own sum of media data fields

        :type startDate: datetime.date
        :type endDate: datetime.date
        :param selectFieldsDict: dict used to filter the media data dicts to retrieve
                                 ex: dict {'verb':'post', 'object_type':'note'} for GooglePlus data
                                     will return dicts with those values present
        :return: count of all the user's favories, shares, comments content within date range
        :rtype: int
        """
        userdataDict = self.getAllData(startDate, endDate, selectFieldsDict)
        allActionsKeys = [self.favoriteskey, self.shareskey, self.commentskey]
        return sum([userdataDict.get(actionkeyname, (0,))[0] for actionkeyname in allActionsKeys])

    ### # # ============== below are util functions ==============

    def _isInSelectDictFields(self, inpDict, inpDictFields):
        """
        returns bool if inpDict has the same key-values of inpDictFields dict

        :param inpDict: current dict to determine if it has inpDictFields keys-values
        :param inpDictFields: dict fields to filter inpDict by
        :type inpDictFields: dict
        :rtype: bool
        """
        # # blank inpDictFields dict defaults to taking the inpDict
        if not inpDictFields: return True
        return all([inpDict.get(k)==inpDictFields[k] for k in inpDictFields.keys()])