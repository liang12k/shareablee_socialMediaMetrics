
***
Note:
-----
feedback: not scalable, first time tackling this type of problem


Improvements:
use pandas to handle the wrangling of mock user data
shorten modulenames, methodnames (refactoring)


Leaving here for future tackling and other users to dive into
***


shareablee_socialMediaMetrics
=============================

Shareablee - interview question: providing a module used to generate social media content metrics
             for twitter, google+ using mock data


Using: PyCharm 3.4.1 (Community Edition) / Python 2.6.7

Note: the date ranges are using datetime.date
-----


--------
Twitter:
--------
To get twitter mock data extract in a list of dicts, args are:
+ status_id string
+ start datetime.datetime
+ end datetime.datetime

from shareablee_socialMediaMetrics.dataextractors.twitter_extractor import getTwitter_userData
ex:
    twitterData = getMediaData('twitter', "286200117457846272",
                            datetime.datetime(2014,1,1), datetime.datetime(2014,8,5))


To get the analytics of the above twitter mock data extract, args are:
+ list of dataset dicts
+ start datetime.datetime
+ end datetime.datetime

from shareablee_socialMediaMetrics.analytics.twitter_analytics import TwitterAnalytics
ex:
    twitterDataAnalytics = TwitterAnalytics(twitterData,
                                            datetime.datetime(2014,1,1),
                                            datetime.datetime(2014,8,5))


--------
Google+:
--------
To get google+ mock data extract in a list of dicts, args are:
+ status_id string
+ start datetime.datetime
+ end datetime.datetime

from shareablee_socialMediaMetrics.dataextractors.googleplus_extractor import getGooglePlus_userData
ex:
    googleplusData = getMediaData('googleplus', "100470681032489535736",
                                datetime.datetime(2014,1,1),
                                datetime.datetime(2014,8,5))


To get the analytics of the above google+ mock data extract, args are:
+ list of dataset dicts
+ start datetime.datetime
+ end datetime.datetime

from shareablee_socialMediaMetrics.analytics.googleplus_analytics import GoogleplusAnalytics
ex:
    googleplusDataAnalytics = GoogleplusAnalytics(googleplusData,
                                                datetime.datetime(2014,1,1),
                                                datetime.datetime(2014,8,5))
