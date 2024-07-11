from flask import render_template, redirect, url_for, flash, request, session

from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.bookings_repository import BookingsRepository
from lib.bookings import Bookings
from datetime import datetime

def spaces_routes(app):
    @app.route('/view-all-spaces', methods=['GET'])
    def view_all_spaces():
        spaces = SpaceRepository(get_flask_database_connection(app)).get_all()
        return render_template('view-all-spaces.html', spaces=spaces)
