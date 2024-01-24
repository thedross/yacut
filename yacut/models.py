from datetime import datetime
from flask import url_for
from urllib.parse import urljoin

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=urljoin(url_for('index_view', _external=True), self.short))

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])
