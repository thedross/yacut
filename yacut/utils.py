import random

from .constants import SYMBOLS_FOR_URL
from .models import URLMap


def check_unique_short_link(short_id):
    if URLMap.query.filter_by(short=short_id).first():
        return False
    return True


def get_unique_short_link():
    short_id = ''.join(random.choices(SYMBOLS_FOR_URL, k=6))
    if check_unique_short_link(short_id):
        return short_id
    return get_unique_short_link()


def check_url_symbols(short_id):
    if short_id is None:
        return False
    return all(symbol in SYMBOLS_FOR_URL for symbol in short_id)