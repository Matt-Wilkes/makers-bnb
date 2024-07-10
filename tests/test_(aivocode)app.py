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

    user = UserRepository(db_connection).find('email.1@gmail.com', 'Password_1')

    page.fill('input[name="email"]', 'email.1@gmail.com')
    page.fill('input[name="password"]', 'Password_1')
    page.click('input[name="submit"]')

    #checking content of home.html
    expect(page.locator('h1')).to_have_text('Home')
    expect(page.locator('._session_email')).to_have_text(user.email)