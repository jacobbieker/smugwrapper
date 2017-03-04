from . import Album, Image
import http
import SmugMug


class AlbumImage(object):
    def __init__(self, album=None, image=None):
        self.album = album
        self.image = image
