import os
from flask import Flask, render_template, redirect, url_for, flash, request, session

from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space

from routes.bookings_routes import bookings_routes
from routes.users_routes import users_routes
from routes.spaces_routes import spaces_routes
from view_space_routes import apply_space_routes
from routes.reservations_routes import reservations_routes

app = Flask(__name__)
app.secret_key = os.urandom(64)

reservations_routes(app)
bookings_routes(app)
apply_space_routes(app)
users_routes(app)
spaces_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))