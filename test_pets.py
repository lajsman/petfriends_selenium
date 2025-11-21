import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def driver(petfriends_driver):
    return petfriends_driver

def test_show_pet_cards(driver):
    driver.get("https://petfriends.skillfactory.ru/my_pets")

    images = driver.find_elements(By.CSS_SELECTOR, "table tbody tr th img")
    names = driver.find_elements(By.XPATH, "//table//tr/td[1]")
    breeds = driver.find_elements(By.XPATH, "//table//tr/td[2]")
    ages = driver.find_elements(By.XPATH, "//table//tr/td[3]")

    for i in range(len(names)):
        assert images[i].get_attribute("src") != "", f"❌ Фото отсутствует у питомца {i+1}"
        assert names[i].text.strip() != "", f"❌ Имя пустое у питомца {i+1}"
        assert breeds[i].text.strip() != "", f"❌ Порода пустая у питомца {i+1}"
        assert ages[i].text.strip() != "", f"❌ Возраст пустой у питомца {i+1}"

def test_show_pet_table(driver):
    driver.get("https://petfriends.skillfactory.ru/my_pets")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.table")))
    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    for i, row in enumerate(rows):
        image = row.find_element(By.XPATH, ".//th/img")
        cells = row.find_elements(By.TAG_NAME, "td")
        assert image.get_attribute("src") != ""
        assert cells[0].text.strip() != ""
        assert cells[1].text.strip() != ""
        assert cells[2].text.strip() != ""
