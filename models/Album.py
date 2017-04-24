import http
import SmugMug


class Album(object):
    def __init__(self, smugmug=None):
        self.description = ""
        self.album_key = None
        self.allow_downloads = False
        self.backprinting = ""
        self.boutique_packaging = "No"
        self.can_rank = False
        self.can_share = False
        self.clean = False
        self.comments = False
        self.download_password = ""
        self.exif = False
        self.family_edit = False
        self.filenames = False
        self.friend_edit = False
        self.geography = False
        self.has_download_password = False
        self.header = "SmugMug"
        self.hide_owner = False
        self.highlight_album_image_uri = ""
        self.image_count = 0
        self.intercept_shipping = "No"
        self.keywords = ""
        self.largest_size = "Original"
        self.name = ""
        self.node_id = ""
        self.original_sizes = 0
        self.packaging_branding = False
        self.password = ""
        self.password_hint = ""
        self.printable = False
        self.printmark_uri = ""
        self.privacy = "Private"
        self.proof_days = 0
        self.protected = False
        self.security_type = "None"
        self.share = False
        self.slideshow = False
        self.smug_searchable = "No"
        self.sort_direction = "Descending"
        self.sort_method = "Position"
        self.square_thumbs = False
        self.template_uri = ""
        self.total_sizes = 0
        self.url_name = ""
        self.url_path = ""
        self.watermark = False
        self.watermark_uri = ""
        self.world_searchable = False

        self.smugmug = smugmug

        self.album_share_uris = {}
        self.user = None
        self.node = None
        self.node_cover_image = ""
        self.folder = None
        self.parent_folders = []
        self.highlight_image = {}
        self.album_images = {}
        self.album_popular_images = {}
        self.album_geo_media = {}
        self.album_comments = {}
        self.album_download = {}
        self.album_prices = {}

    def _unpack_json(self, json_dictionary):
        """ Unpack to dictionary containing the JSON response for the album.
        Used to update values for Album object.
        ":param json_dictionary: Dictionary containing the JSON of the "Response" key, tested for, and assumed to be,
        with '_shorturis' and '_verbosity=1' options enabled for the JSON"""
        album_root = json_dictionary["Album"]

        self.name = album_root["Name"]
        self.allow_downloads = album_root["AllowDownloads"]
        self.description = album_root["Description"]
        self.keywords = album_root["Keywords"]
        self.password_hint = album_root["PasswordHint"]
        self.protected = album_root["Protected"]
        self.sort_direction = album_root["SortDirection"]
        self.sort_method = album_root["SortMethod"]
        self.album_key = album_root["AlbumKey"]
        self.node_id = album_root["NodeID"]
        self.image_count = album_root["ImageCount"]
        self.url_path = album_root["UrlPath"]
        self.can_share = album_root["CanShare"]
        self.node = album_root["Node"]

        return 0

    def refresh(self):
        """ Updates Album object with data from SmugMug """
        if self.album_key is not None:
            if self.smugmug is not None:
                downloader = http.downloader.Downloader(smugmug=self.smugmug)
            else:
                downloader = http.downloader.Downloader()
            data = downloader.refresh_by_key("Album", self.album_key)
            self._unpack_json(data)
        return self

    def update(self):
        """ Updates the SmugMug Album with new data"""
        return self

    def upload(self):
        """ Uploads Album to SmugMug"""
        return self

