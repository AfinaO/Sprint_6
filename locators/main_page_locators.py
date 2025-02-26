# Локаторы для для элементов на главной странице
from selenium.webdriver.common.by import By

class MainPageLocators:
    main_page_header = (By.CLASS_NAME, 'Home_Header__iJKdX')  #заголовок главной страницы
    scooter_logo = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')  #логотип самоката
    yandex_logo = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')  #логотип яндекса
    cookie_button_locator = [By.XPATH, "//button[@id='rcc-confirm-button']"]  #кнопка подтверждения использования куков

    header_order_button = [By.CLASS_NAME, 'Button_Button__ra12g']  #кнопка Заказать сверху страницы
    main_order_button = [By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM']  #кнопка Заказать на главной странице
    page_title = (By.TAG_NAME, 'title')  #локатор для проверки загрузки новой страницы

#локаторы разела Вопросы о важном
    q_how_much = [By.ID, 'accordion__heading-0']  #вопрос Сколько стоит
    answer_how_much = [By.XPATH, '//div[@id="accordion__panel-0"]']  #ответ на вопрос Сколько стоит

    q_several = [By.ID, 'accordion__heading-1']  #вопрос Хочу несколько
    answer_several = [By.XPATH, '//div[@id="accordion__panel-1"]']  #ответ на вопрос Хочу несколько

    q_time = [By.ID, 'accordion__heading-2']  #вопрос Как рассчитывается время
    answer_time = [By.XPATH, '//div[@id="accordion__panel-2"]']  #ответ на вопрос Как рассчитывается время

    q_today = [By.ID, 'accordion__heading-3']  #вопрос Можно ли заказать сегодня
    answer_today = [By.XPATH, '//div[@id="accordion__panel-3"]']  #ответ на вопрос Можно ли заказать сегодня

    q_return = [By.ID, 'accordion__heading-4']  #вопрос Можно ли продлить заказ или вернуть
    answer_return = [By.XPATH, '//div[@id="accordion__panel-4"]']  #ответ на вопрос Можно ли продлить заказ или вернуть

    q_charger = [By.ID, 'accordion__heading-5']  #вопрос Вы привозите зарядку
    answer_charger = [By.XPATH, '//div[@id="accordion__panel-5"]']  #ответ на вопрос Вы привозите заряду

    q_cancel = [By.ID, 'accordion__heading-6']  #вопрос можно ли отменить заказ
    answer_cancel = [By.XPATH, '//div[@id="accordion__panel-6"]']  #ответ на вопрос Можно ли отменить заказ

    q_mkad = [By.ID, 'accordion__heading-7']  #вопрос Я жизу за МКАДом
    answer_mkad = [By.XPATH, '//div[@id="accordion__panel-7"]']  #ответ на вопрос Я жизу за МКАДом

#списки локаторов раздела Вопросы о важном
    questions_locators = [q_how_much,
                          q_several,
                          q_time,
                          q_today,
                          q_return,
                          q_charger,
                          q_cancel,
                          q_mkad]
    answers_locators = [answer_how_much,
                        answer_several,
                        answer_time,
                        answer_today,
                        answer_return,
                        answer_charger,
                        answer_cancel,
                        answer_mkad]