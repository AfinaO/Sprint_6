import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Закрыть окно подтверждения использования куков, если оно есть')
    def close_cookie_popup(self):
        cookie_button = self.get_element(MainPageLocators.cookie_button_locator)
        if cookie_button.is_displayed:
            cookie_button.click()

    @allure.step('Скролл до элемента')
    def scroll_to(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Подождать загрузки элемента')
    def wait_visibility(self, locator):
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located(locator))

    @allure.step('Кликнуть на элемент')
    def click_on(self, locator):
        self.get_element(locator).click()

    @allure.step('Ввести значение в поле ввода')
    def send_keys(self, locator, keys):
        self.get_element(locator).send_keys(keys)

    @allure.step('Получить текст из элемента')
    def get_text(self, locator):
        return self.get_element(locator).text

    @allure.step('Перейти на вторую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Получить URL страницы')
    def get_page_url(self):
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(MainPageLocators.page_title))
        return self.driver.current_url

    @allure.step('Проверить отображение элемента')
    def check_displaying(self, locator):
        return self.get_element(locator).is_displayed()
