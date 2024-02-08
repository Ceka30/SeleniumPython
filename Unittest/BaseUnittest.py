import time
import unittest

from selenium import webdriver

class BaseUnittest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Edge()
        self.driver.maximize_window()


    def test1(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/test/delete_customer.php")
        time.sleep(3)

    def tearDown(self):

        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()

