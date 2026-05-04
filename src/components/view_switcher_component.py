from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent
import allure


class ViewSwitcherComponent(BaseComponent):

    LIST_BUTTON = (By.XPATH, "//button[@class='list']")
    GRID_BUTTON = (By.XPATH, "//button[@class='gallery']")

    @allure.step("Переключитись у List view")
    def switch_to_list(self):
        self.click(self.LIST_BUTTON)

    @allure.step("Переключитись у Grid view")
    def switch_to_grid(self):
        self.click(self.GRID_BUTTON)

    @allure.step("Перевірити наявність кнопок Grid/List")
    def is_displayed(self):
        return (
            self.find(self.LIST_BUTTON).is_displayed() and
            self.find(self.GRID_BUTTON).is_displayed()
        )