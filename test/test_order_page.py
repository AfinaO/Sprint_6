import allure
from conftest import driver
from page_objects.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from testdata import *
import pytest


class TestOrderPage:

    @allure.title('Проверяем позитивный сценарий оформления заказа')
    @allure.description('Тестирование работы формы заказа из двух точек входа на разных наборах данных')
    @pytest.mark.parametrize('button, test_dataset', [(MainPageLocators.header_order_button, DataSet1),
                                                   (MainPageLocators.main_order_button, DataSet2)])
    def test_order_positive(self, driver, button, test_dataset):
        order_page = OrderPage(driver)
        order_page.close_cookie_popup()
        order_page.scroll_to(button)
        order_page.wait_visibility(button)
        order_page.click_on(button)
        order_page.fill_first_form(test_dataset)
        order_page.click_on(OrderPageLocators.next_button_locator)

        order_page.fill_second_form(test_dataset)

        order_page.click_on(OrderPageLocators.order_button_locator)
        order_page.wait_visibility(OrderPageLocators.confirm_button_locator)
        order_page.click_on(OrderPageLocators.confirm_button_locator)

        assert order_page.check_if_confirm_window_displayed(), f'Страница подтверждения заказа не загрузилась'