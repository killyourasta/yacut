from datetime import datetime

from yacut import db

from .constants import SHORT_ID_LENGTH
from .utils import get_unique_short_id


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def _unique_short(self, short_id):
        return URLMap.query.filter_by(short=short_id).first() is not None

    def get_original_url(self):
        return self.original

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        custom_id = data.get('custom_id')
        if custom_id:
            setattr(self, 'short', custom_id)
        else:
            short_url = get_unique_short_id(SHORT_ID_LENGTH)
            while self._unique_short(short_url):
                short_url = get_unique_short_id(SHORT_ID_LENGTH)
            setattr(self, 'short', short_url)

    def to_dict(self, host=''):
        return dict(
            short_link=host + self.short,
            url=self.original,
        )
