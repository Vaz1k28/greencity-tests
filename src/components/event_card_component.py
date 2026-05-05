import allure
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent

class EventCardComponent(BaseComponent):
    EVENT_CARDS = (By.XPATH, "//div[@class='image-container']")
    JOIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Join event')]")
    SIGN_IN_WINDOW = (By.XPATH, "//div[@class='left-side']")

    @allure.step("Click first available action button")
    def click_first_action_button(self):
        self.click(self.JOIN_BUTTON)

    @allure.step("Verify Sign in window appears")
    def wait_for_sign_in_window(self):
        return self.wait.until(
            lambda d: d.find_element(*self.SIGN_IN_WINDOW)
        )