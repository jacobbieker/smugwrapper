#!/usr/bin/env python
from models import  Album, AlbumImage, Folder, Image, Node, Uploader, User, UserProfile
import requests
from requests_oauthlib import OAuth1

OAUTH_ORIGIN = 'https://secure.smugmug.com'
REQUEST_TOKEN_URL = OAUTH_ORIGIN + '/services/oauth/1.0a/getRequestToken'
ACCESS_TOKEN_URL = OAUTH_ORIGIN + '/services/oauth/1.0a/getAccessToken'
AUTHORIZE_URL = OAUTH_ORIGIN + '/services/oauth/1.0a/authorize'

API_ORIGIN = 'https://api.smugmug.com'


class SmugMug(object):

    def __init__(self, api_key=None, oauth_secret=None, api_version="2.0",
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

    def authorize(self, access="Public", permissions="Read"):
        parameters = {"Access": access, "Permissions": permissions}
        requests.get()