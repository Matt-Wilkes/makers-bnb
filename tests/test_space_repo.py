from lib.space_repository import SpaceRepository
from lib.space import Space 


def test_get_all(created_space_repo):
    assert created_space_repo.get_all() == [
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', [])]
    

def test_get_id(created_space_repo):
    assert created_space_repo.get_by_id(1) == Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', [])

def test_create(created_space_repo):
    created_space_repo.create(Space(2, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', []))
    assert created_space_repo.get_all() == [
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', []),
        Space(2, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', [])]

def test_delete(created_space_repo):
    created_space_repo.delete(1)
    assert created_space_repo.get_all() == []

def test_update(created_space_repo):
    created_space_repo.update(1, Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 120, 'UK', 'London', []))
    assert created_space_repo.get_all() == [
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 120, 'UK', 'London', [])]