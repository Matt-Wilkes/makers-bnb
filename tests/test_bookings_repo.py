from lib.bookings_repository import BookingsRepository
from lib.bookings import Bookings

## updated these tests for combined seed

def test_get_all(created_bookings_repo):
    assert created_bookings_repo.get_all() == [
        Bookings(1, 1, 'email.2@gmail.com', [], 'Pending'),
        Bookings(2, 3, 'email.2@gmail.com', [], 'Approved')]

def test_create(created_bookings_repo):
    created_bookings_repo.create(Bookings(3, 4, 'email.2@gmail.com', [], 'Pending' ))
    assert created_bookings_repo.get_all() == [
        Bookings(1, 1, 'email.2@gmail.com', [], 'Pending'),
        Bookings(2, 3, 'email.2@gmail.com', [], 'Approved'),
        Bookings(3, 4, 'email.2@gmail.com', [], 'Pending' )]