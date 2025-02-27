import allure
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполняем форму на первой странице заказа')
    def fill_first_form(self, dataset):
        self.wait_visibility(OrderPageLocators.NAME_LOCATOR)
        self.send_keys(OrderPageLocators.NAME_LOCATOR, dataset.NAME)
        self.send_keys(OrderPageLocators.LAST_NAME_LOCATOR, dataset.LASTNAME)
        self.send_keys(OrderPageLocators.ADDRESS_LOCATOR, dataset.ADDRESS)
        self.click_on(OrderPageLocators.SUBWAY_LOCATOR)
        self.send_keys(OrderPageLocators.SUBWAY_LOCATOR, dataset.SUBWAY)
        self.click_on(OrderPageLocators.SELECTED_ITEM)
        self.send_keys(OrderPageLocators.PHONE_LOCATOR, dataset.PHONE)

    @allure.step('Заполняем форму на второй странице заказа')
    def fill_second_form(self, dataset):
        self.wait_visibility(OrderPageLocators.WHEN_LOCATOR)
        self.click_on(OrderPageLocators.WHEN_LOCATOR)
        self.send_keys(OrderPageLocators.WHEN_LOCATOR, dataset.DATE)
        self.click_on(OrderPageLocators.EMPTY_LOCATOR)  # get rid of calendar popup
        self.click_on(OrderPageLocators.COLOR_LOCATOR)

        self.click_on(OrderPageLocators.TERM_LOCATOR)
        self.click_on(OrderPageLocators.TERM_ROW_LOCATOR)
        self.send_keys(OrderPageLocators.COMMENT_LOCATOR, dataset.COMMENT)

    @allure.step('Проверяем появление окна подтверждения заказа')
    def check_if_confirm_window_displayed(self):
        return self.check_displaying(OrderPageLocators.SHOW_STATUS)
