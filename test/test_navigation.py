import allure
from conftest import driver
from page_objects.main_page import MainPage


class TestNavigation:
    @allure.title('Проверяем переход на главную страницу при клике на лого "Самокат" в шапке')
    def test_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_page()
        main_page.click_on_scooter_logo()
        assert main_page.check_if_main_page_displayed(), f'Главная страница не загрузилась'

    @allure.title('Проверяем переход на страницу "Дзена" при клике на лого "Яндекс в шапке"')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_yandex_logo()
        main_page.switch_to_next_tab()
        cur_url = main_page.get_page_url()
        assert('dzen.ru' in cur_url), f'Ожидаем наличие "dzen.ru" в URL, пришел URL: {cur_url}"'