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
        #checks if space with same name, country, city already exists, does not create new one if it does
        if not [space.name, space.country, space.city] in [[i.name, i.country, i.city] for i in self.get_all()]:
            return self.db_connection.execute('INSERT INTO spaces (description, name, bedrooms, price, country, city, booked_dates, owner_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING name', [space.description, space.name, space.bedrooms, space.price, space.country, space.city, space.booked_dates, space.owner_id])[0]

    def delete(self, id):
        self.db_connection.execute("DELETE FROM spaces WHERE id = %s", [id])

    def update(self, id, space):
        self.db_connection.execute("UPDATE spaces SET description = %s, name = %s, bedrooms = %s, price = %s, country = %s, city = %s, booked_dates = %s WHERE id = %s", [space.description, space.name, space.bedrooms, space.price, space.country, space.city, space.booked_dates, id])

    def find_by_name_description(self,name,description):
        row = self.db_connection.execute("SELECT * FROM spaces WHERE name = %s AND description = %s",[name,description])
        return Space(row[0]['id'], row[0]['description'], row[0]['name'], row[0]['bedrooms'], row[0]['price'], row[0]['country'], row[0]['city'], row[0]['booked_dates'], row[0]['owner_id'])