import pytest
# pytest.skip(allow_module_level=True)

from playwright.sync_api import Page, expect

# Testing list all spaces, filtered
def test_view_all_spaces(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/login")

    page.fill('input[name="email"]', 'email.1@gmail.com')
    page.fill('input[name="password"]', 'Password_1')
    page.click('input[name="submit"]')

    #click link inside home.html
    page.click('._all_spaces')

    #checking content of view-all-spaces.html
    expect(page.locator('h1')).to_have_text('All Spaces')
    expect(page.locator('._name')).to_have_text(['Makers Retreat', 'Makers All-Inclusive', 'Makers Party'])
    expect(page.locator('._name')).not_to_have_text(['Makers Mansion', 'Makers Shed', 'Makers Villa'])