# Локаторы для элементов на странице заказа
from selenium.webdriver.common.by import By

class OrderPageLocators:
#локаторы формы на первой странице заказа
    name_locator = [By.XPATH, "//input[@placeholder='* Имя']"]  #поле Имя
    last_name_locator = [By.XPATH, "//input[@placeholder='* Фамилия']"]  #поле Фамилия
    address_locator = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]  #поле Адрес
    subway_locator = [By.XPATH, "//input[@placeholder='* Станция метро']"]  #поле Станция метро
    selected_item = (By.XPATH, ".//li[@class='select-search__row']")  #выбранный элемент списка станций метро
    phone_locator = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]  #поле Телефон

    next_button_locator = [By.XPATH, "//button[text()='Далее']"]  #кнопка Даее на первой странице заказа

#локаторы формы на второй странице заказа
    when_locator = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]  #поле Когда привезти
    term_locator = [By.XPATH, "//div[@class='Dropdown-control']"]  #выпадающий список На какой срок
    term_row_locator = [By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"]  #значение Сутки в выпадающем списке На какой срок
    color_locator = [By.XPATH, "//input[@class='Checkbox_Input__14A2w']"]  #выбор самоката черного цвета
    comment_locator = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]  #поле Комментарий к заказу
    empty_locator = [By.XPATH, "//div[@class='Order_Content__bmtHS']"]  #локатор для клика по пустому месту страницы
    order_button_locator = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")  #кнопка Заказать

    confirm_button_locator = (By.XPATH, "//button[text()='Да']")  #Кнопка Да для подтверждения заказа
    show_status = (By.XPATH, ".//*[text()='Посмотреть статус']")  #кнопка Посмотреть статус