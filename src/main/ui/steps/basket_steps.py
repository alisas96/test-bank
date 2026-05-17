import allure
from src.main.ui.pages.basket_page import BasketPage
from playwright.sync_api import Page


class BasketSteps:
    def __init__(self, page: Page):
        self.page = page
        self.basket = BasketPage(page)

    @allure.step("Открываем корзину")
    def open_cart(self):
        self.basket.open_cart()
        return self

    @allure.step("Проверяем, что товар {product_name} в корзине")
    def expect_item_in_cart(self, product_name: str):
        self.basket.expect_item_in_cart(product_name)
        return self

    @allure.step("Удаляем товар {product_name}")
    def remove_item(self, product_name: str):
        self.basket.remove_item(product_name)
        return self
    
    @allure.step("Получаем имена товаров")
    def get_items_names(self):
        return self.basket.get_item_names()

    @allure.step("Переходим к созданию заказа")
    def checkout(self):
        return self.basket.checkout()

    @allure.step("Проверяем, что товара {product_name} нет в корзине")
    def expect_item_not_in_cart(self, product_name: str):
        self.basket.expect_item_not_in_cart(product_name)
        return self

    @allure.step("Получаем итоговую стоимость товаров")
    def get_items_total_price(self):
        return self.basket.get_items_total_price()
