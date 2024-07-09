from lib.space_repository import SpaceRepository
from lib.space import Space 

## updated these tests for combined seed

def test_get_all(created_space_repo):
    assert created_space_repo.get_all() == [
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', []),
        Space(2, 'A horrible place to stay', 'Makers Shed', 1, 5, 'UK', 'Burnley', []),
        Space(3, 'A fantastic holiday destination', 'Makers Villa', 1, 5000, 'USA', 'California', [])]
    

def test_get_id(created_space_repo):
    assert created_space_repo.get_by_id(1) == Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', [])

def test_create(created_space_repo):
    created_space_repo.create(Space(4, 'Haunted House', 'Spooky Manor', 13, 1, 'UK', 'Harrow', []))
    assert created_space_repo.get_all() == [
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', []),
        Space(2, 'A horrible place to stay', 'Makers Shed', 1, 5, 'UK', 'Burnley', []),
        Space(3, 'A fantastic holiday destination', 'Makers Villa', 1, 5000, 'USA', 'California', []),
        Space(4, 'Haunted House', 'Spooky Manor', 13, 1, 'UK', 'Harrow', [])]

def test_delete(created_space_repo):
    created_space_repo.delete(4)
    assert created_space_repo.get_all() == [
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', []),
        Space(2, 'A horrible place to stay', 'Makers Shed', 1, 5, 'UK', 'Burnley', []),
        Space(3, 'A fantastic holiday destination', 'Makers Villa', 1, 5000, 'USA', 'California', [])]
    

def test_update(created_space_repo):
    created_space_repo.update(1, Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 120, 'UK', 'London', []))
    assert created_space_repo.get_all() == [
        Space(2, 'A horrible place to stay', 'Makers Shed', 1, 5, 'UK', 'Burnley', []),
        Space(3, 'A fantastic holiday destination', 'Makers Villa', 1, 5000, 'USA', 'California', []),
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 120, 'UK', 'London', [])]