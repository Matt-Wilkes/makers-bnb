import os

from flask import Flask, render_template, redirect, url_for, flash, request, session

from lib.database_connection import get_flask_database_connection
from lib.bookings import Bookings
from lib.space_repository import SpaceRepository
from lib.bookings_repository import BookingsRepository

from lib.forms import StatusForm


def bookings_routes(app):

    @app.route('/bookings', methods=['GET'])
    def get_bookings():
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        user_id = session.get('user_id')  # Assuming you set user_id in session after user login
        if user_id:
            bookings = repository.get_by_requester_id(user_id)
        else:
            bookings = repository.get_all()
        return render_template('bookings/index.html', bookings=bookings)

    @app.route('/bookings/<int:id>', methods=['GET'])
    def get_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        booking = repository.get_by_id(id)
        space_repo = SpaceRepository(connection)
        space = space_repo.get_by_id(booking.spaces_id)
        return render_template('bookings/view.html', booking=booking, space=space)
    
    @app.route('/bookings/<int:id>/delete', methods=['POST'])
    def delete_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        repository.delete(id)
        return redirect(url_for('get_bookings'))
    
    @app.route('/bookings/<int:id>/approve', methods=['POST'])
    def approve_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        repository.approve(id)
        return redirect(url_for('get_bookings'))

    @app.route('/bookings/<int:id>/reject', methods=['POST'])
    def reject_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        repository.reject(id)
        return redirect(url_for('get_bookings'))
