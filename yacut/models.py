import random
import re

from datetime import datetime
from urllib.parse import urljoin

from .constants import (
    BASE_URL,
    CUSTOM_ID_REGEX,
    NUMBER_OF_REQUESTS_ALLOWED,
    ORIGINAL_LINK_LENGTH_MAX,
    SHORT_LINK_LENGTH_AUTO,
    SHORT_LINK_LENGTH_MANUAL,
    SYMBOLS_FOR_URL
)

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LINK_LENGTH_MAX), nullable=False)
    short = db.Column(db.String(SHORT_LINK_LENGTH_MANUAL), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=urljoin(BASE_URL, self.short)
        )

    @staticmethod
    def get_by_short_id(short_id):
        return URLMap.query.filter_by(short=short_id).first()

    @staticmethod
    def create(original_link, custom_id=None):
        def check_unique_short_link(short_id):
            if URLMap.get_by_short_id(short_id):
                return False
            return True

        def check_custom_id_symbols(pattern, string):
            return bool(re.match(pattern, string))

        def get_unique_short_link():
            for _ in range(NUMBER_OF_REQUESTS_ALLOWED):
                short_id = ''.join(random.choices(SYMBOLS_FOR_URL, k=SHORT_LINK_LENGTH_AUTO))
                if check_unique_short_link(short_id):
                    return short_id

        if custom_id:
            if not check_custom_id_symbols(pattern=CUSTOM_ID_REGEX, string=custom_id):
                raise ValueError('Указано недопустимое имя для короткой ссылки')
            if not check_unique_short_link(custom_id):
                raise ValueError('Предложенный вариант короткой ссылки уже существует.')
        else:
            custom_id = get_unique_short_link()

        url_map = URLMap(original=original_link, short=custom_id)
        db.session.add(url_map)
        db.session.commit()

        return url_map
