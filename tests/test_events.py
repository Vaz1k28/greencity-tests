import pytest
import allure


@allure.feature("Events Page")
class TestEventsPage:

    @allure.story("Switch view between Grid and List")
    @allure.title("TC-01: Verify switching between Grid and List view")
    def test_switch_view(self, events_page):

        with allure.step("Verify that Grid and List view toggle buttons are visible"):
            assert events_page.is_view_toggle_visible()

        with allure.step("Click on List view icon"):
            events_page.switch_to_list()

        with allure.step("Verify events are displayed in list view"):
            assert events_page.is_list_view()

        with allure.step("Click on Grid view icon"):
            events_page.switch_to_grid()

        with allure.step("Verify events are displayed in grid view"):
            assert events_page.is_grid_view()


    @allure.story("Unauthorized user tries to join event")
    @allure.title("TC-02: Verify login modal appears when unauthorized user clicks Join")
    def test_join_event_unauthorized(self, events_page):

        with allure.step("Ensure user is not logged in"):
            assert not events_page.is_user_logged_in()

        with allure.step("Select the first available event card"):
            event_card = events_page.get_first_event()

        with allure.step("Click 'Join event' button"):
            event_card.click_join()

        with allure.step("Verify that authorization modal is displayed"):
            assert events_page.is_auth_modal_visible()


    @allure.story("Filter events by date range")
    @allure.title("TC-03: Verify Date Range filter functionality")
    def test_filter_by_date(self, events_page):

        with allure.step("Open Date range filter"):
            events_page.open_date_filter()

        with allure.step("Select date range with expected results"):
            events_page.set_date_range("01.01.2026", "31.12.2026")

        with allure.step("Verify filtered results count is updated"):
            assert events_page.get_results_count() > 0

        with allure.step("Click 'Reset all' button"):
            events_page.reset_filters()

        with allure.step("Verify all events are displayed again"):
            assert events_page.get_results_count() > 10
