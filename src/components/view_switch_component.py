from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent
import allure

class ViewSwitchComponent(BaseComponent):
    LIST_BUTTON = (By.XPATH, "//button[@class='list']")
    GRID_BUTTON = (By.XPATH, "//button[@class='gallery']")

    @allure.step("Switch to list view")
    def switch_to_list(self):
        self.click(self.LIST_BUTTON)

    @allure.step("Switch to grid view")
    def switch_to_grid(self):
        self.click(self.GRID_BUTTON)
