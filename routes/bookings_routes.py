import os
from flask import Flask, render_template, redirect, url_for, flash, request, session
from lib.database_connection import get_flask_database_connection
from lib.bookings_repository import BookingsRepository
from lib.space_repository import SpaceRepository
from helpers.consolidate_bookings import consolidate_bookings

def bookings_routes(app):

    @app.route('/bookings', methods=['GET'])
    def get_bookings():
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        user_id = session.get('email')
        all_bookings = repository.get_by_owner_id_status(user_id,'Pending')
        bookings = consolidate_bookings(all_bookings)
        return render_template('bookings/index.html', bookings=bookings)

    @app.route('/bookings/<int:id>', methods=['GET'])
    def get_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        all_bookings = repository.get_consolidated_by_id(id)
        bookings = consolidate_bookings(all_bookings)
        space = SpaceRepository(connection).get_by_id(bookings['spaces_id'][0])
        return render_template('bookings/view.html', bookings=bookings,space=space) 

    @app.route('/bookings/<int:id>/approve', methods=['POST'])
    def approve_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        booking = repository.get_by_id(id)
        space = SpaceRepository(connection).get_by_id(booking.spaces_id)
        for booking in repository.get_by_date_spaces_id(booking.date,space.id):
            if booking.id == id:
                # Extra work needed to approve all bookings on the same 'trip'
                repository.approve(id)
            else:
                # Extra work needed to approve all bookings on the same 'trip'
                repository.reject(booking.id)
        
        return redirect(url_for('get_bookings'))
    
    @app.route('/bookings/<int:id>/reject', methods=['POST'])
    def reject_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        repository.reject(id)
        # Extra work needed to reject all bookings on the same 'trip'
        return redirect(url_for('get_bookings'))
    