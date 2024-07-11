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
        all_bookings = repository.get_by_owner_id(user_id)
        bookings = consolidate_bookings(all_bookings)
        print('BOOKINGS: ', bookings)
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
