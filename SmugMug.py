#!/usr/bin/env python
import models
import requests
from requests_oauthlib import OAuth1


class SmugMug(object):
    """
    This class is in charge of authentication and overall access to the API
    All getting/setting/changing of information with the API should be handled in the
    appropriate model
    Not used if not being authenticated
    """

    def __init__(self, api_key=None, oauth_secret=None, api_version="v2",
                 secure=False, session_id=None, oauth_token=None,
                 oauth_token_secret=None):
        """Initializes a session."""
        self.api_key = api_key
        self.oauth_secret = oauth_secret
        self.secure = secure
        self.session_id = session_id
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.api_version = api_version
        self.auth = None

    def authorize(self, access="Public", permissions="Read"):
        parameters = {"Access": access, "Permissions": permissions}
        requests.get()
        self.auth = OAuth1(self.api_key, self.oauth_secret, self.oauth_token, self.oauth_token_secret)
