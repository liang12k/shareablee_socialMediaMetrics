#!/usr/bin/env python

import datetime
from shareablee_socialMediaMetrics.datastore import twitter_mockdata

def getTwitter_userData(user_id, startDate, endDate):
    """
        returns the twitter data for a user id from start date to end date
        within a list
        
        user_id: str
        startDate: datetime
        endDate: datetime
    """
    # # TODO -- how to get select status to read, instead of whole data?
    allStatuses = [getattr(twitter_mockdata, status) for status in dir(twitter_mockdata)\
                                                      if isinstance(getattr(twitter_mockdata, status), dict)\
                                                      and not status.startswith('__')]
    
    # # regex detection (?) for the datetime string/formats
    statusDate = lambda inputDateStr: datetime.datetime.strptime(inputDateStr, "%Y-%m-%dT%H:%M:%S")
    return [status for status in allStatuses\
                    if str(user_id)==str(status['status_id'])\
                    and startDate <= statusDate(status['created_at']) <= endDate]