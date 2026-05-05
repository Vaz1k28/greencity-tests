import allure
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class EventsPage(BasePage):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"
    EVENT_CARD = (By.XPATH, "//div[@class='image-container']")

    @allure.step("Open Events page")
    def open(self):
        self.driver.get(self.BASE_URL)

    @allure.step("Wait for events to load")
    def wait_for_events(self):
        self.find(self.EVENT_CARD)

    @allure.step("Get events count")
    def get_events_count(self):
        return len(self.find_all(self.EVENT_CARD))
