import pytest
from selenium import webdriver
from src.pages.events_page import EventsPage

@pytest.fixture
def driver():

    driver = webdriver.Firefox() # Або webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def events_page(driver):
    
    page = EventsPage(driver)
    return page