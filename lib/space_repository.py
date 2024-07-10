from lib.space import Space

class SpaceRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        
    def get_all(self):
        rows = self.db_connection.execute("SELECT * FROM spaces")
        print(rows)
        return [Space(row['id'], row['description'], row['name'], row['bedrooms'], row['price'], row['country'], row['city'], row['booked_dates'],row['owner_id']) for row in rows]
    
    def get_by_id(self,id):
        rows = self.db_connection.execute("SELECT * FROM spaces WHERE id = %s",[id])
        return Space(rows[0]['id'], rows[0]['description'], rows[0]['name'], rows[0]['bedrooms'], rows[0]['price'], rows[0]['country'], rows[0]['city'], rows[0]['booked_dates'], rows[0]['owner_id'])
    
    def create(self, space):
        self.db_connection.execute("INSERT INTO spaces (description, name, bedrooms, price, country, city, booked_dates, owner_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [space.description, space.name, space.bedrooms, space.price, space.country, space.city, space.booked_dates, space.owner_id])
    
    def delete(self, id):
        self.db_connection.execute("DELETE FROM spaces WHERE id = %s", [id])
    
    def update(self, id, space):
        self.db_connection.execute("UPDATE spaces SET description = %s, name = %s, bedrooms = %s, price = %s, country = %s, city = %s, booked_dates = %s WHERE id = %s", [space.description, space.name, space.bedrooms, space.price, space.country, space.city, space.booked_dates, id])