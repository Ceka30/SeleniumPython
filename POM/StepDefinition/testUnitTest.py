import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from POM.Pages.pageBusquedaGoogle import pageBusquedaGoogle


class testUnitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.google = pageBusquedaGoogle(self.driver)

    def test_busquedaGoogle(self):
        self.google.navegar("https://www.google.com/")

        self.google.sendKeys("textarea", "name", "q", "animeFLV" + Keys.TAB, "1")
        #time.sleep(2)
        self.google.clickButton("input", "name", "btnK", "2")
        time.sleep(5)



    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()