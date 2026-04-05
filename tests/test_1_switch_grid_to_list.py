import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

driver = webdriver.Firefox()
driver.get(BASE_URL)
wait = WebDriverWait(driver, 10)

button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='list']")))
button = driver.find_element(By.XPATH, "//button[@class='list']")
button.click()
wait.until(lambda d: button.get_attribute("aria-pressed") == "true")

verification1 = button.get_attribute("aria-pressed")
assert verification1 == "true", f"Помилка: Очікували 'true', але отримали '{verification1}'"
print("✅ ПЕРЕВІРКА УСПІШНА: Кнопка 'Список' активована")


button = driver.find_element(By.XPATH, "//button[@class='gallery']")
button.click()
wait.until(lambda d: button.get_attribute("aria-pressed") == "true")

verification2 = button.get_attribute("aria-pressed")
assert verification2 == "true", f"Помилка: Очікували 'true', але отримали '{verification2}'"
print("✅ ПЕРЕВІРКА УСПІШНА: Кнопка 'Cітка' активована")

driver.quit()
