import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EventsPage:


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # -------------------- BASIC --------------------

    @allure.step("Open Events page")
    def open(self):
        self.driver.get(self.BASE_URL)

    # -------------------- VIEW SWITCH --------------------

    @allure.step("Verify that view toggle buttons are visible")
    def is_view_toggle_visible(self):

        list_btn = self.wait.until(EC.visibility_of_element_located(self.LIST_BUTTON))
        grid_btn = self.wait.until(EC.visibility_of_element_located(self.GRID_BUTTON))
        return list_btn.is_displayed() and grid_btn.is_displayed()

    @allure.step("Switch to List view")
    def switch_to_list(self):

        btn = self.wait.until(EC.element_to_be_clickable(self.LIST_BUTTON))
        btn.click()
        self.wait.until(lambda d: btn.get_attribute("aria-pressed") == "true")

    @allure.step("Switch to Grid view")
    def switch_to_grid(self):

        btn = self.wait.until(EC.element_to_be_clickable(self.GRID_BUTTON))
        btn.click()
        self.wait.until(lambda d: btn.get_attribute("aria-pressed") == "true")

    @allure.step("Check that List view is active")
    def is_list_view(self):

        btn = self.driver.find_element(*self.LIST_BUTTON)
        return btn.get_attribute("aria-pressed") == "true"

    @allure.step("Check that Grid view is active")
    def is_grid_view(self):

        btn = self.driver.find_element(*self.GRID_BUTTON)
        return btn.get_attribute("aria-pressed") == "true"

    # -------------------- JOIN EVENT --------------------

    @allure.step("Click 'Join event' button")
    def click_join_event(self):

        join = self.wait.until(EC.element_to_be_clickable(self.JOIN_BUTTON))
        join.click()

    @allure.step("Verify that Sign In modal is displayed")
    def is_sign_in_visible(self):

        modal = self.wait.until(EC.visibility_of_element_located(self.SIGN_IN_MODAL))
        return modal.is_displayed()

    # -------------------- FILTER --------------------

    @allure.step("Фільтрувати події за календарем")
    def filter_by_calendar(self):
       
    
        calendar_btn = self.wait.until(EC.element_to_be_clickable(self.CALENDAR_BUTTON))
        calendar_btn.click()

        # 2. Чекаємо появи дати в DOM (не обов'язково клікабельності)
        start_date = self.wait.until(EC.presence_of_element_located(self.START_DAY))

        # 3. Клік через JavaScript — він ігнорує прозорий фон 'cdk-overlay-backdrop'
        self.driver.execute_script("arguments[0].click();", start_date)
        
        # 4. Натискаємо кнопку Apply
        apply_btn = self.wait.until(EC.element_to_be_clickable(self.APPLY_BUTTON))
        apply_btn.click()

    @allure.step("Перевірити наявність івентів")
    def is_event_displayed(self):
        try:
            # Очікуємо появи хоча б однієї картки події
            elements = self.wait.until(EC.presence_of_all_elements_located(self.EVENT_CARDS))
            return len(elements) > 0
        except:
            return False