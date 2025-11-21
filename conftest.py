import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def petfriends_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://petfriends.skillfactory.ru/login")
    # TODO: enter valid credentials
    driver.find_element(By.ID,"email").send_keys("")
    driver.find_element(By.ID,"pass").send_keys("")
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    return driver
