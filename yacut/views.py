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
        url_map = URLMap.create(
            original_link=form.original_link.data,
            custom_id=form.custom_id.data
        )
    except ValueError as error:
        flash(str(error))
        return render_template('index.html', form=form)
    return render_template(
        'index.html',
        short_link=url_for(
            LINK_TO_ORIGINAL_FUNCTION,
            short_id=url_map.short,
            _external=True
        ),
        form=form
    )


@app.route('/<short_id>')
def link_to_original(short_id):
    url_map = URLMap.get_by_short_id(short_id)
    if url_map is None:
        abort(404)
    return redirect(url_map.original)
