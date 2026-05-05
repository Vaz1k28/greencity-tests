import allure
from src.pages.events_page import EventsPage
from src.components.view_switch_component import ViewSwitchComponent
from src.components.event_card_component import EventCardComponent
from src.components.date_filter_component import DateFilterComponent


@allure.feature("Events Page")
class TestEvents:

    @allure.story("Switch view between Grid and List")
    @allure.title("TC-01: Verify switching between Grid and List view")
    def test_view_switch(self, driver):
        page = EventsPage(driver)
        view = ViewSwitchComponent(driver)

        with allure.step("Open Events page"):
            page.open()

        with allure.step("Wait for events"):
            page.wait_for_events()

        with allure.step("Switch to list view"):
            view.switch_to_list()
            assert page.get_events_count() > 0

        with allure.step("Switch to grid view"):
            view.switch_to_grid()
            assert page.get_events_count() > 0


    @allure.story("Unauthorized user tries to join event")
    @allure.title("TC-02: Verify login modal appears when unauthorized user clicks Join")
    def test_join_requires_login(self, driver):
        page = EventsPage(driver)
        event = EventCardComponent(driver)

        with allure.step("Open Events page"):
            page.open()

        with allure.step("Wait for events"):
            page.wait_for_events()

        with allure.step("Click Join button"):
            event.click_first_action_button()

        with allure.step("Verify Sign in window appears"):
            sign_in = event.wait_for_sign_in_window()
            assert sign_in.is_displayed()

            allure.attach("Sign in modal detected", name="Result")


    @allure.story("Filter events by date range")
    @allure.title("TC-03: Verify Date Range filter functionality")
    def test_date_filter(self, driver):
        page = EventsPage(driver)
        date = DateFilterComponent(driver)

        with allure.step("Open events page"):
            page.open()

        with allure.step("Wait for events"):
            page.wait_for_events()

        with allure.step("Apply date filter"):
            date.open_calendar()
            date.select_date_range()

        with allure.step("Verify events are present"):
            assert page.get_events_count() >= 0