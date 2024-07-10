class Bookings:
    def __init__(self, id, spaces_id, requester_id, requested_dates, status):
        self.id = id
        self.spaces_id = spaces_id
        self.requester_id = requester_id
        self.requested_dates = requested_dates
        self.status = status
        

    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__
    
    def __repr__(self) -> str:
        return f"Bookings({self.id}, {self.spaces_id}, {self.requester_id}, {self.requested_dates}, {self.status})"