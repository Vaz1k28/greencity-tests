import unittest
from selenium import webdriver
from pages.events_page import EventsPage


class TestViewToggle(unittest.TestCase):

    def test_switch_views(self):

        page = EventsPage(driver)
        page.open()

        assert page.click_list_view() == "true"
        print("✅ Кнопка 'Список' працює")

        assert page.click_gallery_view() == "true"
        print("✅ Кнопка 'Сітка' працює")

        driver.quit()
        
if __name__ == "__main__":
    import unittest
    unittest.main()