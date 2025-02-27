# Локаторы для элементов на странице заказа
from selenium.webdriver.common.by import By


class OrderPageLocators:
    # локаторы формы на первой странице заказа
    NAME_LOCATOR = [By.XPATH, "//input[@placeholder='* Имя']"]  # Поле Имя
    LAST_NAME_LOCATOR = [By.XPATH, "//input[@placeholder='* Фамилия']"]  # Поле Фамилия
    ADDRESS_LOCATOR = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]  # Поле Адрес
    SUBWAY_LOCATOR = [By.XPATH, "//input[@placeholder='* Станция метро']"]  # Поле Станция метро
    SELECTED_ITEM = (By.XPATH, ".//li[@class='select-search__row']")  # Выбранный элемент списка станций метро
    PHONE_LOCATOR = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]  # Поле Телефон

    NEXT_BUTTON_LOCATOR = [By.XPATH, "//button[text()='Далее']"]  # Кнопка Далее на первой странице заказа

    # Локаторы формы на второй странице заказа
    WHEN_LOCATOR = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]  # Поле Когда привезти
    TERM_LOCATOR = [By.XPATH, "//div[@class='Dropdown-control']"]  # Выпадающий список На какой срок
    TERM_ROW_LOCATOR = [By.XPATH,
                        "//div[@class='Dropdown-option' and text()='сутки']"]  # Значение Сутки в выпадающем списке На какой срок
    COLOR_LOCATOR = [By.XPATH, "//input[@class='Checkbox_Input__14A2w']"]  # Выбор самоката черного цвета
    COMMENT_LOCATOR = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]  # Поле Комментарий к заказу
    EMPTY_LOCATOR = [By.XPATH, "//div[@class='Order_Content__bmtHS']"]  # Локатор для клика по пустому месту страницы
    ORDER_BUTTON_LOCATOR = (
    By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")  # Кнопка Заказать

    CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Да']")  # Кнопка Да для подтверждения заказа
    SHOW_STATUS = (By.XPATH, ".//*[text()='Посмотреть статус']")  # Кнопка Посмотреть статус
