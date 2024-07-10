from lib.bookings import Bookings

def test_init(created_bookings):
    assert created_bookings.id == 1
    assert created_bookings.spaces_id == 1
    assert created_bookings.requester_id == 1
    assert created_bookings.requested_dates == []
    assert created_bookings.status == "Pending"
        
def test_is_equal(created_bookings):
    bookings1 = Bookings(1, 1, 1, [], "Pending")
    assert created_bookings == bookings1

def test_string_format(created_bookings):
    assert str(created_bookings) == "Bookings(1, 1, 1, [], Pending)"