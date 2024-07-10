from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from flask import request, render_template, redirect, url_for

def apply_space_routes(app):
    @app.route('/view-space/<id>', methods=['GET'])
    def view(id):
        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        space = space_repository.get_by_id(id)
        return render_template('view-space.html', space=space)
