OAUTH_ORIGIN = 'https://secure.smugmug.com'
REQUEST_TOKEN_URL = OAUTH_ORIGIN + '/services/oauth/1.0a/getRequestToken'
ACCESS_TOKEN_URL = OAUTH_ORIGIN + '/services/oauth/1.0a/getAccessToken'
AUTHORIZE_URL = OAUTH_ORIGIN + '/services/oauth/1.0a/authorize'

API_ORIGIN = 'https://api.smugmug.com'

UPLOAD_URL = "https://upload.smugmug.com/"

URI_BASE = "/api/v2/"

API_BASE = API_ORIGIN + URI_BASE

API_URI = {"Album": API_BASE + "album", "Image": API_BASE + "image", "User": API_BASE + "user",
           "Node": API_BASE + "node", "Folder": API_BASE + "folder"}
