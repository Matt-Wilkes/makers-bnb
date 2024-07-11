class User():
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__
    
    def __str__(self) -> str:
        return f"User({self.id}, {self.email}, {self.password})"