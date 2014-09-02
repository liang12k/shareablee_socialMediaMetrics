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