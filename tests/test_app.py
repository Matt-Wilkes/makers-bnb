from playwright.sync_api import Page, expect

# Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(p_tag).to_have_text("This is the homepage.")

"""
We can render the view_space page
"""
def test_get_view_space(page, test_web_address, db_connection):
    db_connection.seed('seeds/space.sql')
    page.goto(f"http://{test_web_address}/view_space/1")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Makers Mansion")

"""
The view_space page should show the property details (name, description, bedrooms, price (GBP), location)
"""

def test_get_view_space_properties(page, test_web_address, db_connection):
    db_connection.seed('seeds/space.sql')
    page.goto(f"http://{test_web_address}/view_space/1")
    expect(page.get_by_test_id("t-description")).to_have_text("A lovely place to stay")
    expect(page.get_by_test_id("t-bedrooms")).to_have_text("3 Bedrooms")
    expect(page.get_by_test_id("t-price")).to_have_text("£100")
    expect(page.get_by_test_id("t-location")).to_have_text("London, UK")
    
    