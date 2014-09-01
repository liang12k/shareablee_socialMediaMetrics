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
                                    if startDate <= self._getDateTypeFormat(datadict[self.datekey]) <= endDate\
                                    and self._isFitDictFields(datadict, selectFieldsDict)]
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
                    # # store as sum of values for select keys
                    outputDict[k] = (sum([int(num) for num in outputDict[k]]),)
        # # can be taken as: ex: count of tweets, googleplus notes
        outputDict['dicts_with_selectfields_count'] = (len(inpListOfUserDicts),)
        return outputDict

    def getAllFavorites(self, startDate, endDate, selectFieldsDict={}):
        """
        :type startDate: datetime.date
        :type endDate: datetime.date
        :param selectFieldsDict: dict used to filter the media data dicts to retrieve
                                 ex: dict {'verb':'post', 'object_type':'note'} for GooglePlus data
                                     will return dicts with those values present
        :return: count of all the user's favorite content within date range
        """
        return self.getAllData(startDate, endDate, selectFieldsDict).get(self.favoriteskey, (0,))

    def getAllComments(self, startDate, endDate, selectFieldsDict={}):
        """
        :type startDate: datetime.date
        :type endDate: datetime.date
        :param selectFieldsDict: dict used to filter the media data dicts to retrieve
                                 ex: dict {'verb':'post', 'object_type':'note'} for GooglePlus data
                                     will return dicts with those values present
        :return: count of all the user's comment content within date range
        """
        return self.getAllData(startDate, endDate, selectFieldsDict).get(self.commentskey, (0,))

    def getAllShares(self, startDate, endDate, selectFieldsDict={}):
        """
        :type startDate: datetime.date
        :type endDate: datetime.date
        :param selectFieldsDict: dict used to filter the media data dicts to retrieve
                                 ex: dict {'verb':'post', 'object_type':'note'} for GooglePlus data
                                     will return dicts with those values present
        :return: count of all the user's shares content within date range
        """
        return self.getAllData(startDate, endDate, selectFieldsDict).get(self.shareskey, (0,))


    ### # # ============== below are util functions ==============

    def _isFitDictFields(self, inpDict, inpDictFields):
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

    def _getDateTypeFormat(self, inpDate):
        """
        override this method, convert date string to datetime.date

        :param inpDate: input date string format
        :return: datetime.date
        """
        return inpDate