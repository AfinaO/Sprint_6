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
    @pytest.mark.parametrize('button, test_dataset', [(MainPageLocators.HEADER_ORDER_BUTTON, DataSet1),
                                                      (MainPageLocators.MAIN_ORDER_BUTTON, DataSet2)])
    def test_order_positive(self, driver, button, test_dataset):
        order_page = OrderPage(driver)
        order_page.close_cookie_popup()
        order_page.scroll_to(button)
        order_page.wait_visibility(button)
        order_page.click_on(button)
        order_page.fill_first_form(test_dataset)
        order_page.click_on(OrderPageLocators.NEXT_BUTTON_LOCATOR)

        order_page.fill_second_form(test_dataset)

        order_page.click_on(OrderPageLocators.ORDER_BUTTON_LOCATOR)
        order_page.wait_visibility(OrderPageLocators.CONFIRM_BUTTON_LOCATOR)
        order_page.click_on(OrderPageLocators.CONFIRM_BUTTON_LOCATOR)

        assert order_page.check_if_confirm_window_displayed(), f'Страница подтверждения заказа не загрузилась'
