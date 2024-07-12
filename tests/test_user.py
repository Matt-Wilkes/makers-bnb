import pytest
# pytest.skip(allow_module_level=True)

from lib.user import User

def test_init(created_user):
    assert created_user.id == 3
    assert created_user.email == 'email@testing.com'
    assert created_user.password == 'password'

def test_is_equal(created_user):
    user1 = User(3,'email@testing.com', 'password')
    assert created_user == user1

def test_string_format(created_user):
    assert str(created_user) == "User(3, email@testing.com, password)"