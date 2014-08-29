import datetime
from shareablee_socialMediaMetrics.datastore import twitter_mockdata

def getTwitter_userData(user_id, startDate, endDate):
    """
        returns the twitter data for a user id from start date to end date
        within a list
        
        user_id: str
        startDate: datetime.date
        endDate: datetime.date
    """
    # # TODO -- how to get select status to read, instead of whole data?
    allStatuses = [getattr(twitter_mockdata, status) for status in dir(twitter_mockdata)\
                                                      if isinstance(getattr(twitter_mockdata, status), dict)\
                                                      and not status.startswith('__')]
    
    # # TODO -- fine tune to handle hh:mm:ss for start/end dates
    # # regex detection (?) for the datetime string/formats
    status_yyymmddDate = lambda inputDateStr: datetime.datetime.strptime(inputDateStr, "%Y-%m-%dT%H:%M:%S").date()
    # # assuming all status has an 'created_at' key
    return [status for status in allStatuses\
                    if str(user_id)==str(status['status_id'])\
                    and startDate <= status_yyymmddDate(status['created_at']) <= endDate]