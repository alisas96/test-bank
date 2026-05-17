import pytest
from src.main.ui.steps.catalog_steps import CatalogSteps
from src.main.ui.steps.basket_steps import BasketSteps
from src.main.ui.steps.checkout_steps import CheckoutSteps
from playwright.sync_api import Page


@pytest.mark.ui
def test_add_item_and_check_in_cart(auth_page: Page):
    catalog = CatalogSteps(auth_page)
    basket = BasketSteps(auth_page)
    catalog.add_to_cart("Sauce Labs Bike Light")
    basket.open_cart()
    basket.expect_item_in_cart("Sauce Labs Bike Light")


@pytest.mark.ui
def test_add_items_and_check_in_cart(auth_page: Page):
    catalog = CatalogSteps(auth_page)
    basket = BasketSteps(auth_page)
    catalog.add_to_cart("Sauce Labs Bike Light")
    catalog.add_to_cart("Sauce Labs Onesie")
    basket.open_cart()
    basket.expect_item_in_cart("Sauce Labs Bike Light")
    basket.expect_item_in_cart("Sauce Labs Onesie")


@pytest.mark.ui
def test_remove_item_from_cart(auth_page: Page):
    basket = BasketSteps(auth_page)
    catalog = CatalogSteps(auth_page)
    catalog.add_to_cart("Sauce Labs Bike Light")
    basket.open_cart()
    basket.expect_item_in_cart("Sauce Labs Bike Light")
    basket.remove_item("Sauce Labs Bike Light")
    basket.expect_item_not_in_cart("Sauce Labs Bike Light")


@pytest.mark.ui
def test_remove_items_from_cart(auth_page: Page):
    basket = BasketSteps(auth_page)
    catalog = CatalogSteps(auth_page)
    catalog.add_to_cart("Sauce Labs Bike Light")
    catalog.add_to_cart("Sauce Labs Onesie")
    basket.open_cart()
    basket.expect_item_in_cart("Sauce Labs Bike Light")
    basket.expect_item_in_cart("Sauce Labs Onesie")
    basket.remove_item("Sauce Labs Bike Light")
    basket.remove_item("Sauce Labs Onesie")
    basket.expect_item_not_in_cart("Sauce Labs Bike Light")
    basket.expect_item_not_in_cart("Sauce Labs Onesie")


@pytest.mark.ui
def test_checkout_multiple_items(auth_page: Page):
    catalog = CatalogSteps(auth_page)
    basket = BasketSteps(auth_page)
    checkout = CheckoutSteps(auth_page)
    catalog.add_to_cart("Sauce Labs Bike Light")
    catalog.add_to_cart("Sauce Labs Onesie")
    basket.open_cart()
    basket.expect_item_in_cart("Sauce Labs Bike Light")
    basket.expect_item_in_cart("Sauce Labs Onesie")
    basket_total = basket.get_items_total_price()
    basket.checkout()
    checkout.start_checkout(first_name="Test", last_name="User", postal_code="12345")
    checkout_total = checkout.get_items_total_after_continue()
    assert checkout_total == basket_total, "Сумма товаров не совпадает"


@pytest.mark.ui
@pytest.mark.xfail
def test_checkout_without_items(auth_page: Page):
    basket = BasketSteps(auth_page)
    checkout = CheckoutSteps(auth_page)
    basket.open_cart()
    items = basket.get_items_names()
    assert len(items) == 0, "Корзина не пуста"

    basket.checkout()
    checkout.start_checkout(first_name="NewUser", last_name="Nrk", postal_code="12367")
    error_text = checkout.get_error_message_text()
    assert error_text != "", "Не вышла ошибка при оформлении пустой корзины"
