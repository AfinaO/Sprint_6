import pytest
from selenium import webdriver
from constants import Links


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get(Links.MAIN_LINK)
    yield driver
    driver.quit()
