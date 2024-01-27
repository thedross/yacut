import os
import string


SYMBOLS_FOR_URL = string.ascii_letters + string.digits
SHORT_LINK_LENGTH_MANUAL = 16
SHORT_LINK_LENGTH_AUTO = 6
CUSTOM_ID_REGEX = r'^[A-Za-z0-9]{1,16}$'
ORIGINAL_LINK_LENGTH_MAX = 256
BASE_URL = f'http://{os.getenv("HOST", "localhost")}'
LINK_TO_ORIGINAL_FUNCTION = 'link_to_original'
API_ORIGINAL_REQUEST = 'url'
API_SHORT_REQUEST = 'custom_id'
API_ORIGINAL_RESPONSE = 'url'
API_SHORT_RESPONSE = 'short_link'
NUMBER_OF_REQUESTS_ALLOWED = 314
