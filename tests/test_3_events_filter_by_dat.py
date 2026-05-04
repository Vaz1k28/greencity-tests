import unittest
from selenium import webdriver
from src.pages.events_page import EventsPage
from base_test import BaseTest


class TestJoinEvent(BaseTest):

    def test_join_event(self):

        page = EventsPage(self.driver)
        page.open()

        page.click_join_event()
        assert page.is_sign_in_visible()

        print("✅ Логін-вікно з'явилось")
       

if __name__ == "__main__":
    import unittest
    unittest.main()