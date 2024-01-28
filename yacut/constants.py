import re
import string


SYMBOLS_FOR_URL = string.ascii_letters + string.digits
SHORT_LENGTH_MANUAL = 16
SHORT_LENGTH_AUTO = 6
SHORT_REGEX = r'^[' + re.escape(SYMBOLS_FOR_URL) + r']+$'
ORIGINAL_LINK_LENGTH_MAX = 256
LINK_TO_ORIGINAL_FUNCTION = 'link_to_original'
NUMBER_OF_REQUESTS_ALLOWED = 500
