from flask import jsonify, request
from http import HTTPStatus

from . import app, db
from .constants import MAX_SHORT_LENGTH
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import check_unique_short_link, check_url_symbols, get_unique_short_link


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_link(short_id):
    link = URLMap.query.filter_by(short=short_id).first()
    if link is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': link.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data or data['url'] is None:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')

    if 'custom_id' in data:
        custom_id = data.get('custom_id')
        if not check_unique_short_link(custom_id):
            raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
        if not custom_id:
            data['custom_id'] = get_unique_short_link()
        elif not check_url_symbols(custom_id) or len(custom_id) > MAX_SHORT_LENGTH:
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    else:
        data['custom_id'] = get_unique_short_link()

    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED