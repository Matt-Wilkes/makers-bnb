from flask import render_template, redirect, url_for, flash, request, session

from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.bookings_repository import BookingsRepository
from lib.bookings import Bookings
from lib.forms import NewSpaceForm
from datetime import datetime

def spaces_routes(app):
    @app.route('/view-all-spaces', methods=['GET'])
    def view_all_spaces():
        spaces = SpaceRepository(get_flask_database_connection(app)).get_all()
        return render_template('view-all-spaces.html', spaces=spaces)

    @app.route('/view-my-spaces', methods=['GET'])
    def view_my_spaces():
        spaces = SpaceRepository(get_flask_database_connection(app)).get_all()
        return render_template('view-my-spaces.html', spaces=spaces)

    @app.route('/new-space', methods=['GET', 'POST'])
    def new_space():
        form = NewSpaceForm()

        if request.method == 'POST':
            if form.validate_on_submit():
                space = Space(None, form.description.data, form.name.data, form.bedrooms.data, form.price.data, form.country.data, form.city.data, [], session['email'])
                space_return = SpaceRepository(get_flask_database_connection(app)).create(space)
                print('####################')
                print(space_return)
                if space_return:
                    # flash(f'You have created new space named {space_return['name']}')
                    return redirect('/view-my-spaces')
                else:
                    flash('Space with such name and location already exists')
                    return render_template('new-space.html', form=form)
        return render_template('new-space.html', form=form)