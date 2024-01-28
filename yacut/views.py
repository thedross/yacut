from flask import abort, flash, redirect, render_template, url_for

from . import app
from .constants import LINK_TO_ORIGINAL_FUNCTION
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    try:
        return render_template(
            'index.html',
            short_link=url_for(
                LINK_TO_ORIGINAL_FUNCTION,
                short_id=URLMap.create(
                    original_link=form.original_link.data,
                    short=form.custom_id.data,
                    flag=True
                ).short,
                _external=True
            ),
            form=form
        )
    except ValueError as error:
        flash(str(error))
        return render_template('index.html', form=form)


@app.route('/<short_id>')
def link_to_original(short_id):
    url_map = URLMap.get(short_id)
    if url_map is None:
        abort(404)
    return redirect(url_map.original)
