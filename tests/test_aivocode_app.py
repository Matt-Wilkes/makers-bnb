import pytest
# pytest.skip(allow_module_level=True)

from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository


# Testing login.html get request
def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")

    expect(page.locator('label')).to_have_text(['Email', 'Password'])
    expect(page.locator('#email')).to_be_visible()
    expect(page.locator('#password')).to_be_visible()

    expect(page.locator('#submit')).to_be_visible()
    expect(page.locator("#submit")).to_have_value('Login')

# Testing login.html post request
def test_post_login(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/login")

    #checking if user exists in db
    user = UserRepository(db_connection).find('email.1@gmail.com', 'Password_1')

    page.fill('input[name="email"]', 'email.1@gmail.com')
    page.fill('input[name="password"]', 'Password_1')
    page.click('input[name="submit"]')

    #checking content of home.html
    expect(page.locator('h1')).to_have_text('Home')
    expect(page.locator('._session_email')).to_have_text(user.email)

# Testing login.html post request where user does not exist in db
def test_post_login_user_does_not_exist(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/login")

    page.fill('input[name="email"]', 'email.001@gmail.com')
    page.fill('input[name="password"]', 'Password_001')
    page.click('input[name="submit"]')

    #checking content of login.html
    expect(page.locator('h1')).to_have_text('Login')
    expect(page.locator('.alert')).to_have_text('Wrong email/password combination')

# Testing signup.html get request
def test_get_signup(page, test_web_address):
    page.goto(f"http://{test_web_address}/signup")

    expect(page.locator('label')).to_have_text(['Email', 'Password', 'Repeat Password'])
    expect(page.locator('#email')).to_be_visible()
    expect(page.locator('#password')).to_be_visible()
    expect(page.locator('#confirm')).to_be_visible()

    expect(page.locator('#submit')).to_be_visible()
    expect(page.locator("#submit")).to_have_value('Signup')

# Testing signup.html post request
def test_post_signup(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/signup")

    page.fill('input[name="email"]', 'email.000@gmail.com')
    page.fill('input[name="password"]', 'Password_000')
    page.fill('input[name="confirm"]', 'Password_000')
    page.click('input[name="submit"]')

    #checking if user exists in db
    user = UserRepository(db_connection).find('email.000@gmail.com', 'Password_000')

    #checking content of home.html
    expect(page.locator('h1')).to_have_text('Home')
    expect(page.locator('._session_email')).to_have_text(user.email)

# Testing signup.html post request where user already exists in db
def test_post_signup_user_already_exists(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/signup")

    page.fill('input[name="email"]', 'email.1@gmail.com')
    page.fill('input[name="password"]', 'Password_1')
    page.fill('input[name="confirm"]', 'Password_1')
    page.click('input[name="submit"]')

    #checking content of signup.html
    expect(page.locator('h1')).to_have_text('Signup')
    expect(page.locator('.alert')).to_have_text('User with such email already exists')

# Testing signup.html post request where input passwords not matching
def test_post_signup_input_passwords_not_matching(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/signup")

    page.fill('input[name="email"]', 'email.000@gmail.com')
    page.fill('input[name="password"]', 'Password_000')
    page.fill('input[name="confirm"]', 'Password_001')
    page.click('input[name="submit"]')

    #checking content of signup.html
    expect(page.locator('h1')).to_have_text('Signup')
    expect(page.locator('.alert')).to_have_text("Passwords don't match")

def test_logout(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/login")

    #checking if user exists in db
    user = UserRepository(db_connection).find('email.1@gmail.com', 'Password_1')

    page.fill('input[name="email"]', 'email.1@gmail.com')
    page.fill('input[name="password"]', 'Password_1')
    page.click('input[name="submit"]')

    #checking content of home.html
    expect(page.locator('h1')).to_have_text('Home')
    expect(page.locator('._session_email')).to_have_text(user.email)
    expect(page.locator('._logout')).to_have_text('Logout')

    page.click('._logout')

    #checking content of home.html
    expect(page.locator('h1')).to_have_text('Login')