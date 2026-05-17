from playwright.sync_api import Page
import pytest
from src.main.ui.steps.catalog_steps import CatalogSteps


@pytest.mark.ui
def test_count_catalog(auth_page: Page):
    catalog_steps = CatalogSteps(auth_page)
    assert catalog_steps.get_products_count() == 6, "Количество товаров не совпадает"


@pytest.mark.ui
def test_sorted_by_name(auth_page: Page):
    catalog_steps = CatalogSteps(auth_page)
    catalog_steps.sort_items("az")
    names = catalog_steps.get_products_names()
    assert names == sorted(names), "Товары не отсортированы по имени A-Z"


@pytest.mark.ui
def test_sorted_by_name_reverse(auth_page: Page):
    catalog_steps = CatalogSteps(auth_page)
    catalog_steps.sort_items("za")

    names = catalog_steps.get_products_names()
    assert names == sorted(names, reverse=True), "Товары не отсортированы по имени Z-A"


@pytest.mark.ui
def test_sorted_by_price(auth_page: Page):
    catalog_steps = CatalogSteps(auth_page)
    catalog_steps.sort_items("lohi")
    prices = catalog_steps.get_product_prices()

    assert prices == sorted(prices), "Товары не отсортированы по цене low to high"

    catalog_steps.sort_items("hilo")
    prices = catalog_steps.get_product_prices()

    assert prices == sorted(
        prices, reverse=True
    ), "Товары не отсортированы по цене high to low"


@pytest.mark.ui
def test_add_to_cart(auth_page: Page):
    catalog_steps = CatalogSteps(auth_page)
    catalog_steps.add_to_cart("Sauce Labs Bike Light")

    assert catalog_steps.get_cart_count() == 1


@pytest.mark.ui
def test_add_and_remove_onesie_to_cart(auth_page: Page):
    catalog_steps = CatalogSteps(auth_page)
    catalog_steps.add_to_cart("Sauce Labs Onesie")

    assert catalog_steps.get_cart_count() == 1

    catalog_steps.remove_from_cart("Sauce Labs Onesie")

    assert catalog_steps.get_cart_count() == 0


@pytest.mark.ui
def test_product_details_onesie(auth_page: Page):
    catalog_steps = CatalogSteps(auth_page)
    name, price, detail_name, detail_price = catalog_steps.open_product_details(
        product_name="Sauce Labs Onesie",
    )

    assert name == detail_name, "Название продукта не совпадает"
    assert price == detail_price, "Цена продукта не совпадает"


@pytest.mark.ui
def test_remove_item_from_catalog(auth_page: Page):
    catalog_steps = CatalogSteps(auth_page)
    catalog_steps.remove_from_cart("Test.allTheThings() T-Shirt (Red)")
