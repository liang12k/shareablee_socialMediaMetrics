from ..tests import sample_mockdata

def getTwitter_userData(user_id, startDate, endDate):
    """
        returns the twitter data for a user id from start date to end date
        
        user_id: str
        startDate: datetime
        endDate: datetime
    """
    # # read from mock file, return user_id data
    return sample_mockdata.TWITTER_DATA.get(user_id)