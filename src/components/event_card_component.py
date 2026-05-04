from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent
import allure


class EventCardComponent(BaseComponent):

    EVENT_CARDS = (By.XPATH, "//div[@class='image-container']")
    JOIN_BUTTON = (By.XPATH, "(//button[contains(text(), 'Join event')])[1]")

@allure.step("Click 'Join event' button on event card")
def click_join(self):
    with allure.step("Locate 'Join event' button inside the event card"):
        button = self.find(self.JOIN_BUTTON)

    with allure.step("Click on 'Join event' button"):
        button.click()

@allure.step("Verify 'Join event' button is visible on event card")
def is_join_button_visible(self):
    with allure.step("Check visibility of 'Join event' button"):
        return self.find(self.JOIN_BUTTON).is_displayed()