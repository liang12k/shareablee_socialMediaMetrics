"""
This module contains methods on converting the media's data
from its original format to datetime.date type
"""

import datetime

def convertTwitterDate(twitterDate):
    """
    converts Twitter's date field value
    to datetime.date type

    :param twitterDate: twitter's date field value
    :type twitterDate: str
    :return: datetime.date of twitterDate
    """
    if isinstance(twitterDate, str):
        # # TODO -- handle this using regex?
        return datetime.datetime.strptime(twitterDate, "%Y-%m-%dT%H:%M:%S").date()
    return twitterDate

def convertGoogleplusDate(googleplusDate):
    """
    converts Google Plus's date field value
    to datetime.date type

    :param googleplusDate: google plus' date field value
    :type googleplusDate: datetime.datetime
    :return: datetime.date of googleplusDate
    """
    if isinstance(googleplusDate, datetime.datetime):
        return googleplusDate.date()
    return googleplusDate