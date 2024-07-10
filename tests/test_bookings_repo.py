from lib.bookings_repository import BookingsRepository
from lib.bookings import Bookings

## updated these tests for combined seed

def test_get_all(created_bookings_repo):
    assert created_bookings_repo.get_all() == [
        Bookings(1, 1, 2, [], 'Pending'),
        Bookings(2, 3, 2, [], 'Approved')]
    

def test_get_by_id(created_bookings_repo):
    assert created_bookings_repo.get_by_id(1) == Bookings(1, 1, 2, [], 'Pending')
    assert created_bookings_repo.get_by_id(2) == Bookings(2, 3, 2, [], 'Approved')

def test_create_bookings(created_bookings_repo):
    created_bookings_repo.create(Bookings(3, 1, 2, [], 'Pending'))
    assert created_bookings_repo.get_all() == [
        Bookings(1, 1, 2, [], 'Pending'),
        Bookings(2, 3, 2, [], 'Approved'),
        Bookings(3, 1, 2, [], 'Pending')]
    
def test_delete_bookings(created_bookings_repo):
    created_bookings_repo.delete(1)
    assert created_bookings_repo.get_all() == [
        Bookings(2, 3, 2, [], 'Approved')]
    

    
def test_get_by_spaces_id(created_bookings_repo):
    assert created_bookings_repo.get_by_spaces_id(1) == [Bookings(1, 1, 2, [], 'Pending')]
    assert created_bookings_repo.get_by_spaces_id(3) == [Bookings(2, 3, 2, [], 'Approved')]

def test_get_by_requester_id(created_bookings_repo):
    assert created_bookings_repo.get_by_requester_id(2) == [Bookings(1, 1, 2, [], 'Pending'),Bookings(2, 3, 2, [], 'Approved')]

def test_get_by_status(created_bookings_repo):
    assert created_bookings_repo.get_by_status('Approved') == [Bookings(2, 3, 2, [], 'Approved')]
    assert created_bookings_repo.get_by_status('Pending') == [Bookings(1, 1, 2, [], 'Pending')]
    assert created_bookings_repo.get_by_status('Rejected') == []
    assert created_bookings_repo.get_by_status('Cancelled') == []

def test_confirm(created_bookings_repo):
    created_bookings_repo.confirm(1)
    assert created_bookings_repo.get_by_id(1) == Bookings(1, 1, 2, [], 'Approved')
    created_bookings_repo.confirm(2)
    assert created_bookings_repo.get_by_id(2) == Bookings(2, 3, 2, [], 'Approved')