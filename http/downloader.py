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
        self.filters = {}
        self.expansions = {}
        self.smugmug = smugmug

        if isinstance(self.smugmug, SmugMug):
            self.authenticated = True
        else:
            self.authenticated = False

    def request(self, terms, model, returntype="json"):
        if returntype == "json":
            headers = {"Accept": "application/json"}
        else:
            headers = {}

        base_url = http.urls.API_URI[model]

        if self.authenticated:
            # Work with authenticated API
            response = requests.get(base_url + "", headers=headers, auth=self.smugmug.auth)
        else:
            # Not authenticated
            response = requests.get(base_url + "", headers=headers)
        return 0

    def multiget(self, parameters=None):
        return 0

    def check_limit(self):
        return 0

    def refresh_by_key(self, model, key, returntype="json"):
        """
        Get information for a model from SmugMug using its key
        :param model: String containing the name of the model to update
        :param key: Key for the resource (Image, Album, etc)
        :param returntype: Return type for the SmugMug API, defaults to JSON, currently changing does nothing
        :return: Dictionary containing the data from the API Request
        """
        search_url = http.urls.API_URI[model] + key
        headers = {"Accept": "application/json"}
        if self.authenticated:
            auth = self.smugmug.auth
            response_json = requests.get(search_url, headers=headers, auth=auth)
        else:
            response_json = requests.get(search_url, headers=headers)
        response = response_json.json()
        return response["Response"]

    def search(self, model, returntype="json", **kwargs):
        """
            Search, using kwargs, for Album, Image, or User
        :param model: Name of model to search, currently API 2.0 supports search for 'Album', 'Image' and 'User'
        :param returntype: Return type of query, defaults, and currently only, works for JSON
        :return: Results of search in a Python dictionary
        """
        headers = {"Accept": "application/json"}
        search_url = http.urls.API_URI[model] + "!search"
        if model.lower() == "album":
            terms = {"Scope": kwargs.get("scope", ""),
                     "SortDirection": kwargs.get("sort_direction", "Descending"),
                     "SortMethod": kwargs.get("sort_method", "Rank"), "Text": kwargs.get("text", "")}
            if self.authenticated:
                response_json = requests.get(search_url, params=terms, headers=headers, auth=self.smugmug.auth)
            else:
                response_json = requests.get(search_url, params=terms, headers=headers)
            response = response_json.json()
            return response["Response"]
        elif model.lower() == "image":
            terms = {"Scope": kwargs.get("scope", ""), "Keywords": kwargs.get("keywords", ""),
                     "SortDirection": kwargs.get("sort_direction", "Descending"),
                     "SortMethod": kwargs.get("sort_method", "Popular"), "Text": kwargs.get("text", "")}
            if self.authenticated:
                response_json = requests.get(search_url, params=terms, headers=headers, auth=self.smugmug.auth)
            else:
                response_json = requests.get(search_url, params=terms, headers=headers)
            response = response_json.json()
            return response["Response"]
        elif model.lower() == "user":
            terms = {"q": kwargs.get("user", "") }
            if self.authenticated:
                response_json = requests.get(search_url, params=terms, headers=headers, auth=self.smugmug.auth)
            else:
                response_json = requests.get(search_url, params=terms, headers=headers)
            response = response_json.json()
            return response["Response"]
        else: # Not one of the options
            return "Model not recognized, choose between Album, Image, User"
