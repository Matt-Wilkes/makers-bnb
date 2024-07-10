import os

from flask import Flask, render_template, redirect, url_for, flash, request, session

from lib.database_connection import get_flask_database_connection
from lib.bookings import Bookings
from lib.bookings_repository import BookingsRepository


def user_bookings_routes(app):

    @app.route('/my-bookings', methods = ['GET'])
    def get_bookings():
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        bookings = repository.get_all()
        return render_template('bookings/index.html', bookings=bookings)
    
    @app.route('/my-bookings/new', methods = ['GET'])
    def get_new_booking():
        return render_template('bookings/new.html')
    
    @app.route('/my-bookings', methods = ['POST'])
    def post_booking():
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        booking = repository.create(Bookings(None, request.form['space_id'], request.form['user_id'], request.form['date']))
        return redirect('/my-bookings')
    
    @app.route('/my-bookings/<int:id>', methods = ['GET'])
    def get_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        booking = repository.get_by_id(id)
        return render_template('bookings/show.html', booking=booking)
    
    @app.route('/my-bookings/<int:id>/edit', methods = ['GET'])
    def get_edit_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        booking = repository.get_booking(id)
        return render_template('bookings/edit.html', booking=booking)
    
    @app.route('/my-bookings/<int:id>', methods = ['POST'])
    def put_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        booking = repository.update_booking(Bookings(id, request.form['space_id'], request.form['user_id'], request.form['date']))
        return redirect('/my-bookings')
    
    @app.route('/my-bookings/<int:id>', methods = ['POST'])
    def delete_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        repository.delete_booking(id)
        return redirect('/my-bookings')
    
    @app.route('/my-bookings/<int:id>/confirm', methods = ['POST'])
    def confirm_booking(id):
        connection = get_flask_database_connection(app)
        repository = BookingsRepository(connection)
        booking = repository.confirm(id)
        return redirect('/my-bookings')
    

    