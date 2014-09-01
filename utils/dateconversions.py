"""
This module contains methods on converting the media's data
from its original format to datetime.date type
"""

import datetime

def convertTwitterDate(twitterDate):
    """
    converts Twitter's date field value
    to datetime type

    :param twitterDate: twitter's date field value
    :type twitterDate: str
    :return: datetime of twitterDate
    """
    if isinstance(twitterDate, str):
        # # TODO -- handle this using regex?
        twitterDate = datetime.datetime.strptime(twitterDate, "%Y-%m-%dT%H:%M:%S")
    return twitterDate

def convertGoogleplusDate(googleplusDate):
    """
    converts Google Plus' date field value
    to datetime type

    :param googleplusDate: google plus' date field value
    :type googleplusDate: datetime.datetime
    :return: datetime of googleplusDate
    """
    # # leaving this here in case GooglePlus changes its datetime value format
    # if isinstance(googleplusDate, datetime.datetime):
    #     return googleplusDate
    return googleplusDate