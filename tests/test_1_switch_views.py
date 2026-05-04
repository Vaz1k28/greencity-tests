import allure
from src.pages.events_page import EventsPage


@allure.feature("Events Page")
@allure.story("View переключення (Grid / List)")
@allure.title("TC-01: Verify switching between Grid and List view")
def test_switch_views(driver):

    with allure.step("Open Events page"):
        page = EventsPage(driver)
        page.open()  
    with allure.step("Verify that Grid and List toggle buttons are visible"):
        assert page.is_view_toggle_visible()

    with allure.step("Switch to List view"):
        page.switch_to_list()

    with allure.step("Verify that events are displayed in List view"):
        assert page.is_list_view()

    with allure.step("Switch back to Grid view"):
        page.switch_to_grid()

    with allure.step("Verify that events are displayed in Grid view"):
        assert page.is_grid_view()