import SmugMug
import http


class Image(object):
    def __init__(self, title=None, caption=None, keywords=None, hidden=False,
                 altitude=None, latitude=None, longitude=None, watermarked=False,
                 is_video=False, uri=None, image_key=None, collectable=False, can_edit=False, smugmug=None):
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
        self.image_format = ""

        self.smugmug = smugmug


        # Use to hold JSON response for image, possibly, as a cache?
        self.json = None

    def _unpack_json(self, json_dictionary):
        """
        Unpack to dictionary containing the JSON response for the image.
        Used to update values for Image object.
        ":param json_dictionary: Dictionary containing the JSON of the "Response" key
        :return:
        """
        image_root = json_dictionary["Image"]
        self.title = image_root["Title"]
        self.caption = image_root["Caption"]
        self.watermarked = image_root["Watermarked"]
        self.latitude = image_root["Latitude"]
        self.longitude = image_root["Longitude"]
        self.can_edit = image_root["CanEdit"]
        self.hidden = image_root["Hidden"]
        self.collectable = image_root["Collectable"]
        self.altitude = image_root["Altitude"]
        self.image_key = image_root["ImageKey"]
        self.is_video = image_root["IsVideo"]
        self.original_height = image_root["OriginalHeight"]
        self.original_width = image_root["OriginalWidth"]
        self.original_size = image_root["OriginalSize"]
        self.keywords = image_root["KeywordArray"]
        self.image_format = image_root["Format"]

        self.uri = json_dictionary["Uri"]
        return 0

    def get_size(self, size="Original"):
        """ Convenience function to return the URL for the requested size"""
        return self.sizes[size]

    def get_largest(self):
        """ Return largest size"""
        return self.get_size()

    def download(self):
        """ Download copy of image"""
        return 0

    def refresh(self):
        """ Updates Image object with data from SmugMug """
        if self.image_key is not None:
            downloader = http.downloader.Downloader(smugmug=self.smugmug)
            downloader.refresh_by_key("Image", self.image_key)
        return 0

    def update(self):
        """ Updates the SmugMug Image with new data"""
        return 0

    def upload(self):
        """ Uploads image to SmugMug"""
        return 0
