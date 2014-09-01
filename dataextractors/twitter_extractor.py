import datetime
from shareablee_socialMediaMetrics.datastore import twitter_mockdata
from shareablee_socialMediaMetrics.utils.dateconversions import convertTwitterDate

def getTwitter_userData(user_id, startDate, endDate):
    """
    returns the twitter data for a user id from start date to end date
    within a list

    :param user_id: str
    :param startDate: datetime.date
    :param endDate: datetime.date
    """
    # # TODO -- how to get select status to read, instead of whole data?
    allStatuses = [getattr(twitter_mockdata, status) for status in dir(twitter_mockdata)\
                                                      if isinstance(getattr(twitter_mockdata, status), dict)\
                                                      and not status.startswith('__')]
    
    # # TODO -- fine tune to handle hh:mm:ss for start/end dates
    # # assuming all status has an 'created_at' key
    allStatuses= [status for status in allStatuses\
                        if str(user_id)==str(status['status_id'])\
                        and startDate <= convertTwitterDate(status['created_at']).date() <= endDate]
    # # convert the 'created_at' value into datetime.datetime format
    for status in allStatuses:
        if status.get('created_at'):
            status['created_at'] = convertTwitterDate(status['created_at'])
    return allStatuses