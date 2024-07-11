from lib.user_repository import UserRepository
from lib.user import User

def test_get_all(created_user_repo):
    assert created_user_repo.get_all() == [
        User(1, 'email.1@gmail.com', 'Password_1'),
        User(2, 'email.2@gmail.com', 'Password_2')
    ]

def test_create_user(created_user_repo):
    created_user_repo.create(User(3, 'email@testing.com', 'password'))
    assert created_user_repo.get_all() == [
        User(1, 'email.1@gmail.com', 'Password_1'),
        User(2, 'email.2@gmail.com', 'Password_2'),
        User(3, 'email@testing.com', 'password')]
    

def test_find(created_user_repo):
    assert created_user_repo.find('email.1@gmail.com', 'Password_1') == User(1, 'email.1@gmail.com', 'Password_1')
