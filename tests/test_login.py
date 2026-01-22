from pages.login_page import LoginPage


def test_successful_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in page.url

def test_login_with_invalid_credentials(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("invalid_user", "wrong_password")

    error = login_page.get_error_message()
    assert "Username and password do not match" in error