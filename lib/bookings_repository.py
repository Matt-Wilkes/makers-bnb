from lib.bookings import Bookings

class BookingsRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        
    def get_all(self):
        rows = self.db_connection.execute("SELECT * FROM bookings")
        print(rows)
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status']) for row in rows]
    
    def create(self, Bookings):
        self.db_connection.execute("INSERT INTO Bookings(spaces_id, requester_id, requested_dates, status) VALUES (%s, %s, %s, %s)", [Bookings.spaces_id, Bookings.requester_id, Bookings.requested_dates, Bookings.status])