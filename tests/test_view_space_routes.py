from playwright.sync_api import Page, expect

"""
We can render the view_space page
"""

def test_get_view_space(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/view-space/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Makers Mansion")


"""
The view_space page should show the property details (name, description, bedrooms, price (GBP), location)
"""


def test_get_view_space_properties(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/view-space/1")
    expect(page.get_by_test_id("t-description")).to_have_text("A lovely place to stay")
    expect(page.get_by_test_id("t-bedrooms")).to_have_text("3 Bedrooms")
    expect(page.get_by_test_id("t-price")).to_have_text("£100")
    expect(page.get_by_test_id("t-location")).to_have_text("London, UK")
    
"""
The view_space page should show an option to book the property 
"""
def test_get_view_space_has_book_button(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/view-space/1")
    expect(page.get_by_role("button")).to_have_text("Book")
    
"""
The view-space page should show a 'From' date picker and a 'to' date picker
"""
def test_get_view_space_has_date_selector(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/view-space/1")
    expect(page.get_by_test_id("t-requested_dates")).to_have_id("requested_dates")
    

    # this can be added as a feature later
# """
# The view-space page should show a 'From' date picker and a 'to' date picker
# """
# def test_get_view_space_has_date_selectors(page, test_web_address, db_connection):
#     db_connection.seed('seeds/users_seed.sql')
#     page.goto(f"http://{test_web_address}/view-space/1")
#     expect(page.get_by_test_id("t-from_date")).to_have_id("from_date")
#     expect(page.get_by_test_id("t-to_date")).to_have_id("to_date")
    

"""
When I submit the booking form
The space id, account user, date should be sent to the bookings table
"""
def test_post_view_space_post_to_db(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_seed.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill('input[name="email"]', 'email.1@gmail.com')
    page.fill('input[name="password"]', 'Password_1')
    page.click('input[name="submit"]')
    page.goto(f"http://{test_web_address}/view-space/1")
    page.get_by_test_id("t-requested_dates").fill("2024-07-11")
    page.get_by_role("button").click
    page.goto(f"http://{test_web_address}/bookings")
    list_items = page.locator("tr")
    expect(list_items).to_have_count(3)
    

    
    