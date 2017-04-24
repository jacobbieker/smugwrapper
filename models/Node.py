import http
import SmugMug

class Node(object):
    def __init__(self, type=None, node_id=None, node_key=None, uri=None, smugmug=None):
        self.type = type
        self.node_id = node_id
        self.node_key = node_key
        self.uri = uri

        self.date_added = None
        self.date_modified = None
        self.description = ""
        self.has_children = False
        self.is_root = False
        self.security_type = None
        self.response_level = None
        self.name = None
        self.keywords = []
        self.show_cover_image = False
        self.sort_direction = None
        self.sort_index = None
        self.sort_method = None
        self.url_path = None
        self.password_hint = ""
        self.uri_name = None
        self.web_uri = None
        self.hide_owner = False
        self.password = None

        self.highlight_image_uri = None
        self.smug_searchable = False
        self.world_searchable = False
        self.effective_privacy = None
        self.effective_security_type = None

        self.user = None
        self.comments = None
        self.children = None
        self.parents = None

        self.smugmug = smugmug

    def _unpack_json(self, json_dictionary):
        """ Unpack to dictionary containing the JSON response for the album.
        Used to update values for Album object.
        ":param json_dictionary: Dictionary containing the JSON of the "Response" key, tested for, and assumed to be,
        with '_shorturis' and '_verbosity=1' options enabled for the JSON"""
        node_root = json_dictionary["Node"]
        uri_root = json_dictionary["Uris"]

        self.name = node_root["Name"]
        self.allow_downloads = node_root["AllowDownloads"]
        self.description = node_root["Description"]
        self.keywords = node_root["Keywords"]
        self.password_hint = node_root["PasswordHint"]
        self.security_type = node_root["SecurityType"]
        self.sort_direction = node_root["SortDirection"]
        self.sort_method = node_root["SortMethod"]
        self.node_key = node_root["NodeKey"]
        self.node_id = node_root["NodeID"]
        self.show_cover_image = node_root["ShowCoverImage"]
        self.url_path = node_root["UrlPath"]
        self.can_share = node_root["CanShare"]
        self.type = node_root["Type"]
        self.date_added = node_root["DateAdded"]
        self.date_modified = node_root["NodeModified"]
        self.effective_security_type = node_root["EffectiveSecurityType"]
        self.has_children = node_root["HasChildren"]
        self.is_root = node_root["IsRoot"]
        self.web_uri = node_root["WebUri"]

        self.user = uri_root["User"]["Uri"]
        self.comments = uri_root["NodeComments"]["Uri"]
        self.children = uri_root["ChildNodes"]["Uri"]
        self.highlight_image_uri = uri_root["HighlightImage"]["Uri"]
        self.parents = uri_root["ParentNodes"]["Uri"]

        return 0

    def refresh(self):
        """ Updates Album object with data from SmugMug """
        if self.node_key is not None:
            if self.smugmug is not None:
                downloader = http.downloader.Downloader(smugmug=self.smugmug)
            else:
                downloader = http.downloader.Downloader()
            data = downloader.refresh_by_key("Node", self.node_key)
            self._unpack_json(data)
        return self

    def update(self):
        """ Updates the SmugMug Album with new data"""
        return self

    def upload(self):
        """ Uploads Album to SmugMug"""
        return self
