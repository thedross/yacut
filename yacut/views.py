from flask import flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import check_unique_short_link, check_url_symbols, get_unique_short_link


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    custom_id = form.custom_id.data
    if not custom_id:
        custom_id = get_unique_short_link()
    if not check_unique_short_link(custom_id):
        flash('Предложенный вариант короткой ссылки уже существует.')
        return render_template('index.html', form=form)
    if not check_url_symbols(custom_id):
        flash('Указано недопустимое имя для короткой ссылки')
        return render_template('index.html', form=form)
    url = URLMap(
        original=form.original_link.data,
        short=custom_id
    )
    db.session.add(url)
    db.session.commit()
    return render_template('index.html', url=url, form=form)


@app.route('/<short_id>')
def link_to_original(short_id):
    url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url.original)