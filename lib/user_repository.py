from lib.user import User

class UserRepository():
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all(self):
        db_response = self.db_connection.execute("SELECT * from users")
        if db_response:
            return [User(**i) for i in db_response]

    def find(self, email, password):
        db_response = self.db_connection.execute("SELECT * from users WHERE email = %s AND password = %s", [email, password])
        if db_response: return User(**db_response[0])

    def create(self, user):
        if not user.email in [i.email for i in self.get_all()]:
            return self.db_connection.execute('INSERT INTO users (email, password) VALUES (%s, %s) RETURNING id, email', [*user.__dict__.values()][1:])[0]