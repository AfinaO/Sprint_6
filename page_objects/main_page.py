import allure
from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Ждем появления верхней кнопки Заказать и кликаем по нему')
    def go_to_order_page(self):
        self.wait_visibility(MainPageLocators.header_order_button)
        self.click_on(MainPageLocators.header_order_button)

    @allure.step('Ждем появления лого Самокат и кликаем по нему')
    def click_on_scooter_logo(self):
        self.wait_visibility(MainPageLocators.scooter_logo)
        self.click_on(MainPageLocators.scooter_logo)

    @allure.step('Проверяем, загрузилась ли главная страница')
    def check_if_main_page_displayed(self):
        self.wait_visibility(MainPageLocators.main_page_header)
        return self.check_displaying(MainPageLocators.main_page_header)

    @allure.step('Ждем появления лого Яндекса и кликаем по нему')
    def click_on_yandex_logo(self):
        self.wait_visibility(MainPageLocators.yandex_logo)
        self.click_on(MainPageLocators.yandex_logo)

    @allure.step('Скроллим до раздела Важные вопросы')
    def scroll_to_question(self, index):
        self.scroll_to(MainPageLocators.questions_locators[index])

    @allure.step('Ждем появления вопроса')
    def wait_faq_question(self, index):
        self.wait_visibility(MainPageLocators.questions_locators[index])

    @allure.step('Получаем текст вопроса')
    def get_faq_question_text(self, index):
        return self.get_text(MainPageLocators.questions_locators[index])

    @allure.step('Кликаем на вопрос')
    def click_on_question(self, index):
        self.click_on(MainPageLocators.questions_locators[index])

    @allure.step('Ждем появления ответа')
    def wait_faq_answer(self, index):
        self.wait_visibility(MainPageLocators.answers_locators[index])

    @allure.step('Получаем текст ответа')
    def get_faq_answer_text(self, index):
        return self.get_text(MainPageLocators.answers_locators[index])

