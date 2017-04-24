import http
import SmugMug
import Image, Album, Folder, Node, UserProfile, AlbumImage

class User(object):
    def __init__(self, name, smugmug=None):
        self.name = name
        self.account_status = None
        self.first_name = ""
        self.friends_view = False
        self.image_count = 0
        self.is_trial = False
        self.last_name = ""
        self.nick_name = ""
        self.sort_by = None
        self.view_pass_hint = ""
        self.view_password = ""
        self.domain = ""
        self.domain_only = ""
        self.ref_tag = ""
        self.name = ""
        self.plan = None
        self.total_account_size = None
        self.total_uploaded_size = None
        self.quick_share = False
        self.uri = ""

        self.bio_image = None
        self.cover_image = None
        self.user_profile = None
        self.node = None
        self.folder = None
        self.user_albums = None
        self.geo_media = None
        self.popular_media = None
        self.featured_albums = None
        self.recent_images = None
        self.image_search = None
        self.top_keywords = None
        self.url_path_lookup = None
        self.web_uri = None

        self.smugmug = smugmug


    def _follow_uri(self, uri, end_tag):
        """
        Given a uri and tag to get, returns the value of that tag
        :param uri: URI to query
        :param end_tag: Tag, such as "AlbumImage" to search for in the response
        :return:
        """

        return 0

    def _get_object(self, uri, object_type):
        """
        Given a URI and object_type, get the object
        :param uri: URI value
        :param object_type: Type of Object
        :return: Object of object_type located at the URI
        """
        representation = None
        if self.smugmug is not None:
            downloader = http.downloader.Downloader(smugmug=self.smugmug)
        else:
            downloader = http.downloader.Downloader()

        if object_type == "UserProfile":
            representation = UserProfile._unpack_json(downloader.refresh_by_uri(object_type, uri))
        elif object_type == "Node":
            representation = Node._unpack_json(downloader.refresh_by_uri(object_type, uri))
        elif object_type == "Image":
            representation = Image._unpack_json(downloader.refresh_by_uri(object_type, uri))
        elif object_type == "Folder":
            representation = Folder._unpack_json(downloader.refresh_by_uri(object_type, uri))
        elif object_type == "Album":
            representation = Album._unpack_json(downloader.refresh_by_uri(object_type, uri))
        elif object_type == "AlbumImage":
            representation = AlbumImage._unpack_json(downloader.refresh_by_uri(object_type, uri))
        else:
            RuntimeError("Need valid object_type")

        return representation

    def _unpack_json(self, json_dictionary):
        """ Unpack to dictionary containing the JSON response for the album.
        Used to update values for Album object.
        ":param json_dictionary: Dictionary containing the JSON of the "Response" key, tested for, and assumed to be,
        with '_shorturis' and '_verbosity=1' options enabled for the JSON"""
        user_root = json_dictionary["User"]
        uri_root = user_root["Uris"]

        self.name = user_root["Name"]
        self.nick_name = user_root["NickName"]
        self.view_pass_hint = user_root["ViewPassHint"]
        self.quick_share = user_root["QuickShare"]
        self.uri = user_root["Uri"]
        self.web_uri = user_root["WebUri"]
        self.ref_tag = user_root["RefTag"]

        self.bio_image = self._get_object("Image", uri_root["BioImage"]["Uri"])
        self.cover_image = self._get_object("Image", uri_root["CoverImage"]["Uri"])
        self.user_profile = self._get_object("UserProfile", uri_root["UserProfile"]["Uri"])
        self.user_albums = self._get_object("Node", uri_root["Node"]["Uri"])
        self.folder = self._get_object("Folder", uri_root["Folder"]["Uri"])

        return 0

    def refresh(self):
        """ Updates Image object with data from SmugMug """
        if self.nick_name is not None:
            if self.smugmug is not None:
                downloader = http.downloader.Downloader(smugmug=self.smugmug)
            else:
                downloader = http.downloader.Downloader()
            data = downloader.refresh_by_key("User", self.nick_name)
            self._unpack_json(data)
        return self

    def update(self):
        """ Updates the SmugMug Image with new data"""
        return self

    def upload(self):
        """ Uploads image to SmugMug"""
        return self