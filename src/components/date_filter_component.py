from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent
import allure

class DateFilterComponent(BaseComponent):
    CALENDAR = (By.XPATH, "//div[@class='mat-mdc-select-arrow-wrapper']//*[local-name()='svg']")
    START_DAY = (By.XPATH, "//span[contains(@class,'mat-calendar-body-cell-content') and text()=' 1 ']")
    END_DAY = (By.XPATH, "//span[contains(@class,'mat-calendar-body-cell-content') and text()=' 28 ']")

    @allure.step("Open calendar")
    def open_calendar(self):
        self.click(self.CALENDAR)

    @allure.step("Select date range")
    def select_date_range(self):
        self.click(self.START_DAY)
        self.click(self.END_DAY)