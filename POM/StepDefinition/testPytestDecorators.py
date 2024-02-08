import time

import allure
import pytest

from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from POM.Pages.pageBusquedaGoogle import pageBusquedaGoogle

@pytest.fixture(scope='module')
def setUp():
    global driver
    global busqueda

    driver = webdriver.Edge()
    busqueda = pageBusquedaGoogle(driver)

    busqueda.navegar("https://www.google.com/")
    driver.maximize_window()

    yield

    driver.close()

def getData():
    return [
        "Animefft"
    ]

@pytest.mark.usefixtures("setUp")
@pytest.mark.parametrize("texto", getData())
def test_BusquedaGoogle(texto):
    try:
        busqueda.sendKeys("textarea", "name", "q", str(texto) + Keys.TAB, "1")
        time.sleep(1)
        busqueda.clickButton("input", "name", "btnK", "2")
        time.sleep(3)
        assert texto in busqueda.getText("h3","class", "LC20lb MBeuO DKV0Md","1")
        allure.attach(driver.get_screenshot_as_png(), name="Busqueda Completa", attachment_type=AttachmentType.PNG)
    except AssertionError as ex:
        print(ex)
        raise




