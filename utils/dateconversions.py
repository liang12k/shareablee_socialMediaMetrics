"""
This module contains methods on converting the media's data
from its original format to datetime.date type
"""

import datetime

def convertTwitterDate(dateString):
    """
    converts Twitter's datestring to datetime.date type

    :param dateString: twitter's datestring
    :return: datetime.date of dateString
    """
    # # TODO -- handle this using regex?
    return datetime.datetime.strptime(dateString, "%Y-%m-%dT%H:%M:%S").date()