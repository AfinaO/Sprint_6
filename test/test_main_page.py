import allure

import testdata
from page_objects.main_page import MainPage
from conftest import driver
from testdata import QuestionsData
import pytest


class TestMainPageFaq:
    @allure.title('Проверяем секцию "Вопросы о важном"')
    @allure.description('Проверяем правильность текстов вопросов и ответов')
    @pytest.mark.parametrize('question, answer', testdata.get_all_questions_data())
    def test_faq_section(self, driver, question, answer):
        main_page = MainPage(driver)
        index = QuestionsData.questions.index(question)
        main_page.close_cookie_popup()
        main_page.scroll_to_question(index)
        main_page.wait_faq_question(index)
        cur_question = main_page.get_faq_question_text(index)
        assert cur_question == question, f'Неверный текст вопроса. Ожидаем: {question}, пришло: {cur_question}'

        main_page.click_on_question(index)
        main_page.wait_faq_answer(index)
        cur_answer = main_page.get_faq_answer_text(index)
        assert cur_answer == answer, f'Неверный текст ответа. Ожидаем: {answer}, пришло: {cur_answer}'

