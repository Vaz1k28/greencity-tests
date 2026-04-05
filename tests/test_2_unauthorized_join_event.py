import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

driver = webdriver.Firefox()
driver.get(BASE_URL)
wait = WebDriverWait(driver, 10)

join_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Join event')]")))
join_button = driver.find_element(By.XPATH, "//div[@class='btn-group']//button[contains(@class, 'primary-global-button')]")
join_button.click()

sign_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='greenStyle']")))
sing_button = driver.find_element(By.XPATH, "//button[@class='greenStyle']")
assert sing_button.is_displayed()

print("✅ ТЕСТ УСПІШНИЙ: Логін-вікно з'явилося!")

driver.quit()
