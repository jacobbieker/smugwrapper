import requests
from requests_oauthlib import OAuth1
from SmugMug import SmugMug
import http.urls


class Downloader(object):
    """
    Downloader takes care of GET, and similar requests
    """

    def __init__(self, smugmug=None):
        """ Initialization, needs SmugMug for authentication"""
        self.rate_limit = 0
        self.rate_reset = 0
        self.hit_limit = False

        if isinstance(smugmug, SmugMug):
            self.authenticated = True
        else:
            self.authenticated = False

    def request(self, model=None):
        
        return 0

    def filters(self, filters=None):
        return 0

    def expansion(self, expansion=None):
        return 0

    def multiget(self, parameters=None):
        return 0

    def check_limit(self):
        return 0
