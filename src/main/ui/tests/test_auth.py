from playwright.sync_api import Page
import pytest
from src.main.ui.steps.login_steps import LoginSteps
from src.main.ui.steps.catalog_steps import CatalogPage


@pytest.mark.ui
def test_auth_page(page: Page):
    login_steps = LoginSteps(page)
    login_steps.open_login_page()
    login_steps.login("standard_user", "secret_sauce")

    assert page.url == "https://www.saucedemo.com/inventory.html"


@pytest.mark.ui
def test_auth_page_locked_user(page: Page):
    login_steps = LoginSteps(page)
    login_steps.open_login_page()
    login_steps.login("locked_out_user", "secret_sauce")

    assert page.url == "https://www.saucedemo.com/"

    error_text = login_steps.get_error_text()
    assert "locked out" in error_text


@pytest.mark.ui
def test_logout(auth_page: Page):
    catalog = CatalogPage(auth_page)
    catalog.logout()

    assert auth_page.url == "https://www.saucedemo.com/"


@pytest.mark.ui
def test_logout_visual_user(page: Page):
    login_steps = LoginSteps(page)
    catalog = CatalogPage(page)
    login_steps.open_login_page()
    login_steps.login("visual_user", "secret_sauce")

    catalog.logout()
    assert page.url == login_steps.LOGIN_URL, "Ошибка логаута"
