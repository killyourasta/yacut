from flask import flash, redirect, render_template, request

from . import app, db
from .constants import NOT_UNIQUE_LINK_MESSAGE
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data
        if custom_id:
            if URLMap.query.filter_by(short=custom_id).first():
                flash(NOT_UNIQUE_LINK_MESSAGE.format(custom_id), 'error')
                return render_template('index.html', form=form)

        data = {'url': original_link, 'custom_id': custom_id}
        url_map = URLMap()
        url_map.from_dict(data)
        db.session.add(url_map)
        db.session.commit()
        flash(request.root_url + url_map.short, 'short_link')
    return render_template('index.html', form=form)


@app.route('/<short_url>')
def original_url_redirect_view(short_url):
    return redirect(
        URLMap.query.filter_by(short=short_url).first_or_404().original)
