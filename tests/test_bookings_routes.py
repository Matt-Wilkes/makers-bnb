import pytest
# pytest.skip(allow_module_level=True)

from playwright.sync_api import Page, expect


def test_get_view_space(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/bookings")

    expect(page.locator("h1")).to_have_text("My Bookings")
    list_items = page.locator("li")

    expect(list_items).to_have_count(2)
    expect(list_items).to_have_text([
        "Makers Mansion - Pending",
        "Makers Villa - Approved"
    ])
    