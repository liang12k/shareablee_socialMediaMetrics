from shareablee_socialMediaMetrics.datastore import googleplus_mockdata

def getGooglePlus_userData(user_id, startDate, endDate):
    """
        returns the google plus data for a user id from start date to end date
        within a list

        user_id: str
        startDate: datetime.date
        endDate: datetime.date
    """
    # # TODO -- how to get select status to read, instead of whole data?
    allActivities = [getattr(googleplus_mockdata, activity) for activity in dir(googleplus_mockdata)\
                                                          if isinstance(getattr(googleplus_mockdata, activity), dict)\
                                                          and not activity.startswith('__')]

    # # TODO -- fine tune to handle hh:mm:ss for start/end dates
    activity_yyymmddDate = lambda inputDate: inputDate.date()
    # # assuming all activity has an 'updated' key
    return [activity for activity in allActivities\
                    if str(user_id)==str(activity['user_id'])\
                    and startDate <= activity_yyymmddDate(activity['updated']) <= endDate]