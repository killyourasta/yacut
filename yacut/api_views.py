import re
from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .constants import (CUSTOM_ID_CHECK_RE, ERROR_SHORT_URL, ID_NOT_FREE,
                        MISSING_REQUEST, NOT_FOUND_ID, REQUEST_INV_URL_MESSAGE,
                        REQUEST_NO_URL_MESSAGE, URL_CHECK_RE)
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(MISSING_REQUEST)

    url = data.get('url')
    custom_id = data.get('custom_id')

    if not url:
        raise InvalidAPIUsage(REQUEST_NO_URL_MESSAGE)
    if not re.match(URL_CHECK_RE, url):
        raise InvalidAPIUsage(REQUEST_INV_URL_MESSAGE)

    if custom_id:
        if len(custom_id) > 16:
            raise InvalidAPIUsage(
                ERROR_SHORT_URL, HTTPStatus.BAD_REQUEST)
        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise InvalidAPIUsage(
                ID_NOT_FREE.format(custom_id)
            )
        if not re.match(CUSTOM_ID_CHECK_RE, custom_id):
            raise InvalidAPIUsage(ERROR_SHORT_URL)

    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()

    return jsonify(url_map.to_dict(request.root_url)), HTTPStatus.CREATED


@app.route('/api/id/<string:short>/', methods=['GET'])
def get_url(short):
    url_map = URLMap.query.filter_by(short=short).first()
    if not url_map:
        raise InvalidAPIUsage(NOT_FOUND_ID, HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.get_original_url()}), HTTPStatus.OK
