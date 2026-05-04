from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.components.view_switcher_component import ViewSwitcherComponent
from src.components.event_card_component import EventCardComponent
from src.components.filter_panel_component import FilterPanelComponent


class EventsPage:
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"
  
    LIST_BUTTON = (By.XPATH, "//button[@class='list']")
    GALLERY_BUTTON = (By.XPATH, "//button[@class='gallery']")

    CALENDAR = (By.XPATH, "//div[@class='mat-mdc-select-arrow-wrapper']//*[local-name()='svg']")
    START_DAY = (By.XPATH, "//span[contains(@class, 'mat-calendar-body-cell-content') and text()=' 1 ']")
    END_DAY = (By.XPATH, "//span[contains(@class, 'mat-calendar-body-cell-content') and text()=' 28 ']")

    EVENT_CARD = (By.XPATH, "//div[@class='image-container']")
  
    JOIN_BUTTON = (By.XPATH, "(//button[contains(text(), 'Join event')])[2]")
    SIGN_IN = (By.XPATH, "//h1[normalize-space()='Welcome back!']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.view_switcher = ViewSwitcherComponent(driver)
        self.event_card = EventCardComponent(driver)
        self.filter_panel = FilterPanelComponent(driver)
        self.search = SearchComponent(driver)



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
        join.click()

    def is_sign_in_visible(self):
        sign = self.wait.until(EC.element_to_be_clickable(self.SIGN_IN))
        return sign.is_displayed()


    def is_view_toggle_visible(self):
        return self.is_visible(self.GRID_BUTTON) and self.is_visible(self.LIST_BUTTON)

    def switch_to_list(self):
        self.click(self.LIST_BUTTON)

    def switch_to_grid(self):
        self.click(self.GRID_BUTTON)

    def is_list_view(self):
        return "list" in self.get_attribute(self.EVENT_CARDS, "class")

    def is_grid_view(self):
        return "grid" in self.get_attribute(self.EVENT_CARDS, "class")

    def get_first_event(self):
        element = self.find_elements(self.EVENT_CARDS)[0]
        return EventCard(self.driver, element)

    def is_auth_modal_visible(self):
        return self.is_visible(self.AUTH_MODAL)

    def is_user_logged_in(self):
        # адаптуй під свій UI
        return False

    def open_date_filter(self):
        self.click(self.DATE_FILTER)

    def set_date_range(self, start, end):
        # залежить від реалізації календаря
        pass

    def reset_filters(self):
        self.click(self.RESET_BUTTON)

    def get_results_count(self):
        text = self.get_text(self.RESULTS_COUNT)
        return int(text.split()[0])

    def enter_search(self, text):
        self.type(self.SEARCH_INPUT, text)

    def submit_search(self):
        self.click(self.SEARCH_BUTTON)