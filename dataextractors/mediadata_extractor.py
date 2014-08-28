import twitter_extractor
import googleplus_extractor

def extractorMethodsDict():
    """
        contains a dict to of media data extractor methods
    """
    return {
                'twitter' :    twitter_extractor.getTwitter_userData,
                'googleplus' : googleplus_extractor.getGooglePlus_userData,
            }

def getMediaData(mediaTypeString="", user_id="", startDate=None, endDate=None):
    """
        returns the media data from start date to end date
        
        mediaTypeString: str
        user_id: str
        startDate: datetime
        endDate: datetime
    """
    extractMethod = extractorMethodsDict().get(mediaTypeString.lower())
    if not extractMethod:
        raise KeyError("media type unrecognized: " + str(mediaTypeString))
    return extractMethod(user_id, startDate, endDate)
    