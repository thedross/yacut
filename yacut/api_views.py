from flask import jsonify, request
from http import HTTPStatus

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_link(short_id):
    url_map = URLMap.get_by_short_id(short_id)
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data or data['url'] is None:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')

    custom_id = data.get('custom_id')
    try:
        url_map = URLMap.create(original_link=data['url'], custom_id=custom_id)
    except ValueError as error:
        raise InvalidAPIUsage(f'{str(error)}')
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
