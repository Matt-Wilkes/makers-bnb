from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.bookings import Bookings
from lib.user_repository import UserRepository
from lib.bookings_repository import BookingsRepository
from flask import request, render_template, redirect, url_for, session
from datetime import datetime



def apply_space_routes(app):
    @app.route('/view-space/<id>', methods=['GET'])
    def view(id):
        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        bookings_repository = BookingsRepository(connection)
        space = space_repository.get_by_id(id)
        available_bookings = bookings_repository.get_by_spaces_id_available(id)
        available_dates = []
        for booking in available_bookings:
            if booking.date > datetime.today().date():
                available_dates.append(booking.date)
                sorted(available_dates)
                print(booking.date)
            
        return render_template('spaces/view-space.html', space=space, available_dates=available_dates)
    
    @app.route('/view-space/<id>', methods=['POST'])
    def book(id):
        connection = get_flask_database_connection(app)
        booking_repository = BookingsRepository(connection)
        requested_date = request.form['available_dates']
        user_id = session['email']
        booking = booking_repository.get_by_date_spaces_id(requested_date, id)
        booking_repository.request_booking(user_id, booking.id)
        return redirect(url_for('confirmation'))
    
    @app.route('/confirmation', methods=['GET'])
    def confirmation():
        return render_template('spaces/confirmation.html')
        
