from config.settings import BASE_URL
from pages.login_page import LoginPage

def test_invalid_login(page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login("test@example.com", "password123")

    assert page.get_by_text("Your email or password is incorrect!").is_visible()