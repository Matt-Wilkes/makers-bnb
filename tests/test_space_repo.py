import pytest
# pytest.skip(allow_module_level=True)

from lib.space_repository import SpaceRepository
from lib.space import Space

## updated these tests for combined seed

def test_get_all(created_space_repo):
    assert created_space_repo.get_all() == [
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', [],'email.1@gmail.com'),
        Space(2, 'A horrible place to stay', 'Makers Shed', 1, 5, 'UK', 'Burnley', [], 'email.1@gmail.com'),
        Space(3, 'A fantastic holiday destination', 'Makers Villa', 1, 5000, 'USA', 'California', [], 'email.1@gmail.com'),
        Space(4, 'Hunt grizzly bears, catch salmon', 'Makers Retreat', 0, 10000, 'USA', 'Alaska', [], 'email.2@gmail.com'),
        Space(5, 'All you can eat and more', 'Makers All-Inclusive', 1, 2000, 'Spain', 'Tenerife', [], 'email.2@gmail.com'),
        Space(6, 'Throw the wildest party in East London', 'Makers Party', 2, 1000, 'UK', 'London', [], 'email.2@gmail.com')]


def test_get_id(created_space_repo):
    assert created_space_repo.get_by_id(1) == Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', [],'email.1@gmail.com')

def test_create(created_space_repo):
    created_space_repo.create(Space(7, 'Haunted House', 'Spooky Manor', 13, 1, 'UK', 'Harrow', [], 'email.1@gmail.com'))
    assert created_space_repo.get_all() == [
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', [], 'email.1@gmail.com'),
        Space(2, 'A horrible place to stay', 'Makers Shed', 1, 5, 'UK', 'Burnley', [], 'email.1@gmail.com'),
        Space(3, 'A fantastic holiday destination', 'Makers Villa', 1, 5000, 'USA', 'California', [], 'email.1@gmail.com'),
        Space(4, 'Hunt grizzly bears, catch salmon', 'Makers Retreat', 0, 10000, 'USA', 'Alaska', [], 'email.2@gmail.com'),
        Space(5, 'All you can eat and more', 'Makers All-Inclusive', 1, 2000, 'Spain', 'Tenerife', [], 'email.2@gmail.com'),
        Space(6, 'Throw the wildest party in East London', 'Makers Party', 2, 1000, 'UK', 'London', [], 'email.2@gmail.com'),
        Space(7, 'Haunted House', 'Spooky Manor', 13, 1, 'UK', 'Harrow', [], 'email.1@gmail.com')
    ]

def test_delete(created_space_repo):
    created_space_repo.delete(7)
    assert created_space_repo.get_all() == [
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 100, 'UK', 'London', [], 'email.1@gmail.com'),
        Space(2, 'A horrible place to stay', 'Makers Shed', 1, 5, 'UK', 'Burnley', [], 'email.1@gmail.com'),
        Space(3, 'A fantastic holiday destination', 'Makers Villa', 1, 5000, 'USA', 'California', [], 'email.1@gmail.com'),
        Space(4, 'Hunt grizzly bears, catch salmon', 'Makers Retreat', 0, 10000, 'USA', 'Alaska', [], 'email.2@gmail.com'),
        Space(5, 'All you can eat and more', 'Makers All-Inclusive', 1, 2000, 'Spain', 'Tenerife', [], 'email.2@gmail.com'),
        Space(6, 'Throw the wildest party in East London', 'Makers Party', 2, 1000, 'UK', 'London', [], 'email.2@gmail.com')]


def test_update(created_space_repo):
    created_space_repo.update(1, Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 120, 'UK', 'London', [], 'email.1@gmail.com'))
    assert created_space_repo.get_all() == [
        Space(2, 'A horrible place to stay', 'Makers Shed', 1, 5, 'UK', 'Burnley', [], 'email.1@gmail.com'),
        Space(3, 'A fantastic holiday destination', 'Makers Villa', 1, 5000, 'USA', 'California', [], 'email.1@gmail.com'),
        Space(4, 'Hunt grizzly bears, catch salmon', 'Makers Retreat', 0, 10000, 'USA', 'Alaska', [], 'email.2@gmail.com'),
        Space(5, 'All you can eat and more', 'Makers All-Inclusive', 1, 2000, 'Spain', 'Tenerife', [], 'email.2@gmail.com'),
        Space(6, 'Throw the wildest party in East London', 'Makers Party', 2, 1000, 'UK', 'London', [], 'email.2@gmail.com'),
        Space(1, 'A lovely place to stay', 'Makers Mansion', 3, 120, 'UK', 'London', [], 'email.1@gmail.com')]
    


