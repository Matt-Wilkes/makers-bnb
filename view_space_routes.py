from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.bookings import Bookings
from lib.bookings_repository import BookingsRepository
from lib.user import User
from lib.user_repository import UserRepository
from flask import request, render_template, redirect, url_for

def apply_space_routes(app):
    @app.route('/view-space/<id>', methods=['GET'])
    def view(id):
        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        space = space_repository.get_by_id(id)
        return render_template('view-space.html', space=space)
    
    @app.route('/view-space/<id>', methods=['POST'])
    def book(id):
        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        booking_repository = BookingsRepository(connection)
        user_repository = UserRepository(connection)
        requested_dates = request.form['requested_dates']
        email = request.form['session_email']
        booking = Bookings(None, id, email, [requested_dates], "Pending")
        booking_repository.create(booking)

        print(requested_dates)
        print(id)
        print(email)
        
        return redirect(f"/view-space/{id}")