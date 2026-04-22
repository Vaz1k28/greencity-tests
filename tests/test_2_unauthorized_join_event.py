from base_test import BaseTest
from pages.events_page import EventsPage


class TestCalendarFilter(BaseTest):

    def test_calendar_filter(self):
        page = EventsPage(self.driver)
        page.open()

        page.filter_by_calendar()
        assert page.is_event_displayed()

        print("✅ Календарний фільтр працює")
        
if __name__ == "__main__":
    import unittest
    unittest.main()