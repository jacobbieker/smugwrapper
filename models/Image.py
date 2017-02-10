import requests
from requests_oauthlib import OAuth1
import SmugMug


class Image(object):
    def __init__(self, title=None, caption=None, keywords=None, hidden=False,
                 altitude=None, latitude=None, longitude=None, watermarked=False,
                 is_video=False, uri=None, image_key=None, collectable=False, can_edit=False):
        self.title = title
        self.caption = caption
        self.keywords = keywords
        self.hidden = hidden
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude
        self.watermarked = watermarked
        self.is_video = is_video
        self.uri = uri
        self.image_key = image_key
        self.collectable = collectable
        self.can_edit = can_edit

        self.original_height = 0
        self.original_width = 0
        self.original_size = 0


    def get_comments(self):
        """ Returns comments associated with image"""
        return 0

    def get_size(self, size="Original"):
        """ Convienience function to return the URL for the requested size"""
        return 0

    def get_metadata(self):
        """ Returns metadata for the image"""
        return 0

    def get_prices(self):
        """ Return prices for image"""
        return 0

    def get_sizes(self):
        """ Return available sizes"""
        return 0

    def get_size_details(self):
        """ Return detailed size information for image"""
        return 0

    def get_largest(self):
        """ Return largest size"""
        return 0

    def get_owner(self):
        """ Return owner username"""
        return 0

    def get_album(self):
        """ Return album that image is part of"""
        return 0

    def get_point_of_interest(self):
        """ Return point of interest for image"""
        return 0

    def get_regions(self):
        """ Get Regions for image"""
        return 0

    def get_point_of_interest_crops(self):
        """ Returns PointOfInterest Crops for image"""
        return 0

    def download(self):
        """ Return download for image"""
        return 0
