import allure
from src.pages.events_page import EventsPage


# -------------------- TC-01 --------------------

@allure.feature("Events Page")
@allure.story("Switch view between Grid and List")
@allure.title("TC-01: Verify switching between Grid and List view")
def test_switch_view(driver):

    with allure.step("Open Events page"):
        page = EventsPage(driver)
        page.open()

    with allure.step("Check view toggle buttons are visible"):
        assert page.is_view_toggle_visible()

    with allure.step("Switch to List view"):
        page.switch_to_list()
        assert page.is_list_view()

    with allure.step("Switch back to Grid view"):
        page.switch_to_grid()
        assert page.is_grid_view()


# -------------------- TC-02 --------------------

@allure.feature("Events Page")
@allure.story("Unauthorized user tries to join event")
@allure.title("TC-02: Verify login modal appears when unauthorized user clicks Join")
def test_join_event_unauthorized(driver):

    with allure.step("Open Events page"):
        page = EventsPage(driver)
        page.open()

    with allure.step("Click Join event button"):
        page.click_join_event()

    with allure.step("Verify Sign In modal is displayed"):
        assert page.is_sign_in_visible()


# -------------------- TC-03 --------------------

@allure.feature("Events Page")
@allure.story("Filter events by date range")
@allure.title("TC-03: Verify Date Range filter functionality")
def test_filter_by_date(driver):

    with allure.step("Open Events page"):
        page = EventsPage(driver)
        page.open()

    with allure.step("Apply date filter using calendar"):
        page.filter_by_calendar()

    with allure.step("Verify event is displayed after filtering"):
        assert page.is_event_displayed()