from lib.bookings import Bookings

class BookingsRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        
    def get_all(self):
        rows = self.db_connection.execute("SELECT * FROM bookings")
        print(rows)
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status'], row['owner_id']) for row in rows]
    
    def get_by_id(self,id):
        rows = self.db_connection.execute("SELECT * FROM bookings WHERE id = %s",[id])
        return Bookings(rows[0]['id'], rows[0]['spaces_id'], rows[0]['requester_id'], rows[0]['requested_dates'], rows[0]['status'])
    
    def create(self, bookings):
        self.db_connection.execute("INSERT INTO bookings (spaces_id, requester_id, requested_dates, status, owner_id) VALUES (%s, %s, %s, %s,%s)", [bookings.spaces_id, bookings.requester_id, bookings.requested_dates, bookings.status])

    def delete(self, id):
        self.db_connection.execute("DELETE FROM bookings WHERE id = %s", [id])
    
    def get_by_spaces_id(self, spaces_id):
        rows = self.db_connection.execute("SELECT * FROM bookings WHERE spaces_id = %s",[spaces_id])
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status'], row['owner_id']) for row in rows]
    
    def get_by_requester_id(self, requester_id):
        rows = self.db_connection.execute("SELECT * FROM bookings WHERE requester_id = %s",[requester_id])
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status'], row['owner_id']) for row in rows]
    
    def get_by_status(self, status):
        rows = self.db_connection.execute("SELECT * FROM bookings WHERE status = %s",[status])
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status'], row['owner_id']) for row in rows]
    
    def approve(self,id):
        self.db_connection.execute("UPDATE bookings SET status = 'Approved' WHERE id = %s",[id])

    def reject(self,id):
        self.db_connection.execute("UPDATE bookings SET status = 'Rejected' WHERE id = %s",[id])
    
    def cancel(self,id):
        self.db_connection.execute("UPDATE bookings SET status = 'Cancelled' WHERE id = %s",[id])

    def get_by_owner_id(self,owner_id):
        rows = self.db_connection.execute("SELECT * FROM bookings WHERE owner_id = %s",[owner_id])
        return [Bookings(row['id'], row['spaces_id'], row['requester_id'], row['requested_dates'], row['status'], row['ownder_id']) for row in rows]