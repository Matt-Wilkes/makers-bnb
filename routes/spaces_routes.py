from flask import render_template, redirect, url_for, flash, request, session

from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository

def spaces_routes(app):
    @app.route('/view-all-spaces', methods=['GET'])
    def view_all_spaces():
        spaces = SpaceRepository(get_flask_database_connection(app)).get_all()
        return render_template('view-all-spaces.html', spaces=spaces)
