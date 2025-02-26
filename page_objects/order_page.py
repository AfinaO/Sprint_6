import allure
from locators.order_page_locators import OrderPageLocators
from page_objects.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Заполняем форму на первой странице заказа')
    def fill_first_form(self, dataset):
        self.wait_visibility(OrderPageLocators.name_locator)
        self.send_keys(OrderPageLocators.name_locator, dataset.name)
        self.send_keys(OrderPageLocators.last_name_locator, dataset.lastname)
        self.send_keys(OrderPageLocators.address_locator, dataset.address)

        self.click_on(OrderPageLocators.subway_locator)
        self.send_keys(OrderPageLocators.subway_locator, dataset.subway)
        self.click_on(OrderPageLocators.selected_item)

        self.send_keys(OrderPageLocators.phone_locator, dataset.phone)

    @allure.step('Заполняем форму на второй странице заказа')
    def fill_second_form(self, dataset):
        self.wait_visibility(OrderPageLocators.when_locator)
        self.click_on(OrderPageLocators.when_locator)
        self.send_keys(OrderPageLocators.when_locator, dataset.date)
        self.click_on(OrderPageLocators.empty_locator) #get rid of calendar popup
        self.click_on(OrderPageLocators.color_locator)

        self.click_on(OrderPageLocators.term_locator)
        self.click_on(OrderPageLocators.term_row_locator)
        self.send_keys(OrderPageLocators.comment_locator, dataset.comment)

    @allure.step('Проверяем появление окна подтверждения заказа')
    def check_if_confirm_window_displayed(self):
        return self.check_displaying(OrderPageLocators.show_status)

