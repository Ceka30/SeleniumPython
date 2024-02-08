import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from POM.Pages.pageBusquedaGoogle import pageBusquedaGoogle

def setup_function(function):
    global driver
    global busqueda

    driver = webdriver.Edge()
    busqueda = pageBusquedaGoogle(driver)

    busqueda.navegar("https://www.google.com/")
    driver.maximize_window()

def teardown_function(function):
    driver.close()

def test_BusquedaGoogle():
    busqueda.sendKeys("textarea", "name", "q", "animeFLV" + Keys.TAB, "1")
    # time.sleep(2)
    busqueda.clickButton("input", "name", "btnK", "2")
    time.sleep(5)






