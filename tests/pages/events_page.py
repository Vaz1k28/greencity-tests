from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EventsPage:
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    # Locators
    LIST_BUTTON = (By.XPATH, "//button[@class='list']")
    GALLERY_BUTTON = (By.XPATH, "//button[@class='gallery']")

    CALENDAR = (By.XPATH, "//div[@class='mat-mdc-select-arrow-wrapper']//*[local-name()='svg']")
    START_DAY = (By.XPATH, "//span[contains(@class, 'mat-calendar-body-cell-content') and text()=' 1 ']")
    END_DAY = (By.XPATH, "//span[contains(@class, 'mat-calendar-body-cell-content') and text()=' 28 ']")

    EVENT_CARD = (By.XPATH, "//div[@class='image-container']")

    JOIN_BUTTON = (By.XPATH, "(//button[contains(text(), 'Join event')])[2]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.BASE_URL)

    def click_list_view(self):
        button = self.wait.until(EC.element_to_be_clickable(self.LIST_BUTTON))
        button.click()
        self.wait.until(lambda d: button.get_attribute("aria-pressed") == "true")
        return button.get_attribute("aria-pressed")

    def click_gallery_view(self):
        button = self.wait.until(EC.element_to_be_clickable(self.GALLERY_BUTTON))
        button.click()
        self.wait.until(lambda d: button.get_attribute("aria-pressed") == "true")
        return button.get_attribute("aria-pressed")



    def filter_by_calendar(self):
        calendar = self.wait.until(EC.element_to_be_clickable(self.CALENDAR))
        calendar.click()

        start = self.wait.until(EC.element_to_be_clickable(self.START_DAY))
        start.click()

        end = self.wait.until(EC.element_to_be_clickable(self.END_DAY))
        end.click()

    def is_event_displayed(self):
        event = self.wait.until(EC.visibility_of_element_located(self.EVENT_CARD))
        return event.is_displayed()

    def click_join_event(self):
        join = self.wait.until(EC.element_to_be_clickable(self.JOIN_BUTTON))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", join)
        join.click()

    def is_sign_in_visible(self):
        sign = self.wait.until(EC.visibility_of_element_located(self.SIGN_IN_BUTTON))
        return sign.is_displayed()
