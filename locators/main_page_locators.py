# Локаторы для для элементов на главной странице
from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_HEADER = (By.CLASS_NAME, 'Home_Header__iJKdX')  # Заголовок главной страницы
    SCOOTER_LOGO = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')  # Логотип самоката
    YANDEX_LOGO = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')  # Логотип яндекса
    COOKIE_BUTTON_LOCATOR = [By.XPATH, "//button[@id='rcc-confirm-button']"]  # Кнопка подтверждения использования куков
    HEADER_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g']  # Кнопка Заказать сверху страницы
    MAIN_ORDER_BUTTON = [By.CLASS_NAME,
                         'Button_Button__ra12g.Button_Middle__1CSJM']  # Кнопка Заказать на главной странице
    PAGE_TITLE = (By.TAG_NAME, 'title')  # Локатор для проверки загрузки новой страницы

    # локаторы раздела Вопросы о важном
    Q_HOW_MUCH = [By.ID, 'accordion__heading-0']  # Вопрос Сколько стоит
    ANSWER_HOW_MUCH = [By.XPATH, '//div[@id="accordion__panel-0"]']  # Ответ на вопрос Сколько стоит

    Q_SEVERAL = [By.ID, 'accordion__heading-1']  # Вопрос Хочу несколько
    ANSWER_SEVERAL = [By.XPATH, '//div[@id="accordion__panel-1"]']  # Ответ на вопрос Хочу несколько

    Q_TIME = [By.ID, 'accordion__heading-2']  # Вопрос Как рассчитывается время
    ANSWER_TIME = [By.XPATH, '//div[@id="accordion__panel-2"]']  # Ответ на вопрос Как рассчитывается время

    Q_TODAY = [By.ID, 'accordion__heading-3']  # Вопрос Можно ли заказать сегодня
    ANSWER_TODAY = [By.XPATH, '//div[@id="accordion__panel-3"]']  # Ответ на вопрос Можно ли заказать сегодня

    Q_RETURN = [By.ID, 'accordion__heading-4']  # Вопрос Можно ли продлить заказ или вернуть
    ANSWER_RETURN = [By.XPATH, '//div[@id="accordion__panel-4"]']  # Ответ на вопрос Можно ли продлить заказ или вернуть

    Q_CHARGER = [By.ID, 'accordion__heading-5']  # Вопрос Вы привозите зарядку
    ANSWER_CHARGER = [By.XPATH, '//div[@id="accordion__panel-5"]']  # Ответ на вопрос Вы привозите заряду

    Q_CANCEL = [By.ID, 'accordion__heading-6']  # Вопрос можно ли отменить заказ
    ANSWER_CANCEL = [By.XPATH, '//div[@id="accordion__panel-6"]']  # Ответ на вопрос Можно ли отменить заказ

    Q_MKAD = [By.ID, 'accordion__heading-7']  # Вопрос Я жизу за МКАДом - "жизу" не ошибка, так на сайте
    ANSWER_MKAD = [By.XPATH, '//div[@id="accordion__panel-7"]']  # Ответ на вопрос Я жизу за МКАДом

    # Списки локаторов раздела Вопросы о важном
    questions_locators = [Q_HOW_MUCH,
                          Q_SEVERAL,
                          Q_TIME,
                          Q_TODAY,
                          Q_RETURN,
                          Q_CHARGER,
                          Q_CANCEL,
                          Q_MKAD]
    answers_locators = [ANSWER_HOW_MUCH,
                        ANSWER_SEVERAL,
                        ANSWER_TIME,
                        ANSWER_TODAY,
                        ANSWER_RETURN,
                        ANSWER_CHARGER,
                        ANSWER_CANCEL,
                        ANSWER_MKAD]