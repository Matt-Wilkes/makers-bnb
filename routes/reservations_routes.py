import os

from flask import Flask, render_template, redirect, url_for, flash, request, session

from lib.database_connection import get_flask_database_connection
from lib.bookings import Bookings
from lib.space_repository import SpaceRepository
from lib.bookings_repository import BookingsRepository
from helpers.consolidate_bookings import consolidate_bookings

def reservations_routes(app):
    @app.route('/reservations', methods=['GET'])
    def get_reservations():
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        user_id = session.get('email')
        all_reservations = repository.get_by_requester_id(user_id)
        reservations = consolidate_bookings(all_reservations)

        return render_template('reservations/index.html', reservations=reservations)

    @app.route('/reservations/<int:id>', methods=['GET'])
    def get_reservation(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        reservation = repository.get_by_id(id)
        space_repo = SpaceRepository(connection)
        space = space_repo.get_by_id(reservation.spaces_id)
        return render_template('reservations/view.html', reservation=reservation, space=space)
    
    @app.route('/reservations/<int:id>/delete', methods=['POST'])
    def delete_reservation(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        repository.delete(id)
        return redirect(url_for('get_reservations'))
    
    @app.route('/reservations/<int:id>/cancel', methods=['POST'])
    def cancel_reservation(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        repository.cancel(id)
        return redirect(url_for('get_reservations'))
    
    