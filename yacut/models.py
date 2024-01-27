import random
import re

from datetime import datetime
from flask import url_for

from .constants import (
    LINK_TO_ORIGINAL_FUNCTION,
    NUMBER_OF_REQUESTS_ALLOWED,
    ORIGINAL_LINK_LENGTH_MAX,
    SHORT_LINK_LENGTH_AUTO,
    SHORT_LINK_LENGTH_MANUAL,
    SHORT_REGEX,
    SYMBOLS_FOR_URL
)

from yacut import db


ALREADY_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
TRY_AGAIN = 'Попробуйте еще раз, превышено количество попыток.'
UNCORRECT_SHORT = 'Указано недопустимое имя для короткой ссылки'
UNCORRECT_ORIGINAL = 'Превышена допустимая длина оригинальной ссылки'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LINK_LENGTH_MAX), nullable=False)
    short = db.Column(db.String(SHORT_LINK_LENGTH_MANUAL),
                      nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for(
                LINK_TO_ORIGINAL_FUNCTION,
                short_id=self.short,
                _external=True
            )
        )

    @staticmethod
    def get(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def create(original_link, short=None, from_form=False):
        def get_unique_short_link():
            for _ in range(NUMBER_OF_REQUESTS_ALLOWED):
                short_id = ''.join(
                    random.choices(SYMBOLS_FOR_URL, k=SHORT_LINK_LENGTH_AUTO)
                )
                if not URLMap.get(short_id):
                    return short_id
            raise ValueError(TRY_AGAIN)

        if short and not from_form:
            if len(original_link) > ORIGINAL_LINK_LENGTH_MAX:
                raise ValueError(UNCORRECT_ORIGINAL)
            if (not re.match(pattern=SHORT_REGEX, string=short)
               or len(short) > SHORT_LINK_LENGTH_MANUAL):

                raise ValueError(UNCORRECT_SHORT)
            if URLMap.get(short=short):
                raise ValueError(ALREADY_EXISTS)
        elif not short:
            short = get_unique_short_link()

        url_map = URLMap(original=original_link, short=short)
        db.session.add(url_map)
        db.session.commit()

        return url_map
