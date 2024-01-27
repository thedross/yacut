from http import HTTPStatus

from flask import jsonify, request

from .error_handlers import InvalidAPIUsage
from .models import URLMap

from . import app

NOT_FOUND_MESSAGE = 'Указанный id не найден'
URL_REQUIRED_MESSAGE = '"url" является обязательным полем!'
NO_DATA_MESSAGE = 'Отсутствует тело запроса'


@app.route('/api/id/<short>/', methods=['GET'])
def get_original_link(short):
    url_map = URLMap.get(short=short)
    if url_map is None:
        raise InvalidAPIUsage(NOT_FOUND_MESSAGE, HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(NO_DATA_MESSAGE)
    if 'url' not in data or data['url'] is None:
        raise InvalidAPIUsage(URL_REQUIRED_MESSAGE)

    short = data.get('custom_id')
    try:
        url_map = URLMap.create(original_link=data['url'], short=short)
    except ValueError as error:
        raise InvalidAPIUsage(f'{str(error)}')
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
