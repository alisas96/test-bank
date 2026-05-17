import allure
from src.main.ui.pages.checkout_page import CheckoutPage
from playwright.sync_api import Page


class CheckoutSteps:
    def __init__(self, page: Page):
        self.page = page
        self.checkout = CheckoutPage(page)

    @allure.step("Начинаем процесс создания заказа")
    def start_checkout(self, first_name: str, last_name: str, postal_code: str):
        self.checkout.start_checkout(first_name, last_name, postal_code)
        return self

    @allure.step("Завершаем создание заказа")
    def finish_checkout(self):
        self.checkout.finish_checkout()
        return self

    @allure.step("Получаем сообщение об ошибке")
    def get_error_message_text(self):
        return self.checkout.get_error_text()

    @allure.step("Получаем сообщение об успешно созданном заказе")
    def get_success_message_text(self):
        return self.checkout.get_success_text()

    @allure.step("Начинаем процесс создания заказа")
    def get_items_total_after_continue(self):
        return self.checkout.get_item_total_after_continue()
