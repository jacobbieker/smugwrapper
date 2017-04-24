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
        self.

        self.smugmug = smugmug
