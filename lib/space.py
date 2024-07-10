class Space:
    def __init__(self, id, description, name, bedrooms, price, country, city, booked_dates, owner_id):
        self.id = id
        self.description = description
        self.name = name
        self.bedrooms = bedrooms
        self.price = price
        self.country = country
        self.city = city
        self.booked_dates = booked_dates
        self.owner_id = owner_id

    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__
    
    def __str__(self) -> str:
        return f"Space({self.id}, {self.description}, {self.name}, {self.bedrooms}, {self.price}, {self.country}, {self.city}, {self.booked_dates}, {self.owner_id})"