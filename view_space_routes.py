from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.bookings import Bookings
from lib.bookings_repository import BookingsRepository
from flask import request, render_template, redirect, url_for

import calendar
from datetime import datetime



def apply_space_routes(app):
    @app.route('/view-space/<id>', methods=['GET'])
    def view(id):
        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        space = space_repository.get_by_id(id)
        cal= calendar.Calendar()
        current_month = datetime.now().month
        current_year = datetime.now().year
        month_dates = [date for date in cal.itermonthdates(current_year, current_month)]
        available_dates = []
        for date in month_dates:
            # date = datetime.date 
            # datetime.today() datetime.datetime
            if date > datetime.today().date() and date not in space.booked_dates:
                available_dates.append(date)
            
        return render_template('view-space.html', space=space, available_dates=available_dates)
    
    @app.route('/view-space/<id>', methods=['POST'])
    def book(id):
        connection = get_flask_database_connection(app)
        booking_repository = BookingsRepository(connection)
        requested_dates = request.form['available_dates']
        booking = booking_repository.get_by_requested_dates_spaces_id(requested_dates, id)
        booking_repository.set_pending(booking.id)
        return render_template('reservations/index.html')
