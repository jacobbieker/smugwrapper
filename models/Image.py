import SmugMug
import requests
from http.downloader import Downloader
import http.urls


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
        self.metadata = {}
        self.comments = {}
        self.prices = {}
        self.sizes = {}
        self.album = {}
        self.owner = None
        self.size_details = {}
        self.point_of_interest = {}
        self.point_of_interest_crops = {}
        self.regions = {}


        # Use to hold JSON response for image, possibly, as a cache?
        self.json = None

    def get_size(self, size="Original"):
        """ Convenience function to return the URL for the requested size"""
        return 0

    def get_largest(self):
        """ Return largest size"""
        return self.get_size()

    def download(self):
        """ Download copy of image"""
        return 0

    def refresh(self):
        """ Updates Image object with data from SmugMug """
        if self.image_key is not None:
            downloader = Downloader()
            downloader.refresh_by_key("Image", self.image_key)
        return 0

    def update(self):
        """ Updates the SmugMug Image with new data"""
        return 0

    def upload(self):
        """ Uploads image to SmugMug"""
        return 0
