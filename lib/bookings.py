class Bookings:
    def __init__(self, id, spaces_id, requester_id, date, status, owner_id):
        self.id = id
        self.spaces_id = spaces_id
        self.requester_id = requester_id
        self.date = date
        self.status = status
        self.owner_id = owner_id
        

    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__
    
    def __str__(self) -> str:
        return f"Bookings({self.id}, {self.spaces_id}, {self.requester_id}, {self.date}, {self.status})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    