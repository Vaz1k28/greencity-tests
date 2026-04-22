import unittest
from selenium import webdriver
from pages.events_page import EventsPage


class TestJoinEvent(unittest.TestCase):

    def test_join_event(self):
        driver = webdriver.Firefox()
        driver.maximize_window()

        page = EventsPage(driver)
        page.open()

        page.click_join_event()
        assert page.is_sign_in_visible()

        print("✅ Логін-вікно з'явилось")

if __name__ == "__main__":
    import unittest
    unittest.main()