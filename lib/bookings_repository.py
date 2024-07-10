from lib.bookings import Bookings

class BookingsRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        
    def get_all(self):
        rows = self.db_connection.execute("SELECT * FROM bookings")
        print(rows)
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status']) for row in rows]