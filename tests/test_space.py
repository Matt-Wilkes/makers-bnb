import pytest
# pytest.skip(allow_module_level=True)

from lib.space import Space

def test_init(created_space):
    assert created_space.id == 1
    assert created_space.description == "A space for testing"
    assert created_space.name == "Test Space"
    assert created_space.bedrooms == 2
    assert created_space.price == 100
    assert created_space.country == "UK"
    assert created_space.city == "London"
    assert created_space.booked_dates == []
    assert created_space.owner_id == "email.1@gmail.com"

def test_is_equal(created_space):
    space1 = Space(1, "A space for testing", "Test Space", 2, 100, "UK", "London", [], 'email.1@gmail.com')
    assert created_space.owner_id == 'email.1@gmail.com'

def test_string_format(created_space):
    assert str(created_space) == "Space(1, A space for testing, Test Space, 2, 100, UK, London, [], email.1@gmail.com)"