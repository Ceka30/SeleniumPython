from selenium.webdriver.common.by import By
from POM.Pages.WebBase.webBasePage import webBasePage


class pageBusquedaGoogle(webBasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def sendKeys(self, etiqueta, atributo, valor, texto, index):
        driver = self.driver
        try:
            xpath = "(//"+etiqueta+"[@"+atributo+"='"+valor+"'])["+index+"]"
            super().waitUntilElementIsVisible(xpath)
            element = driver.find_element(By.XPATH, xpath)
            if not super().isDisplayed(element):
                print("Elemento No Desplegado")
            if not super().isEnabled(element):
                print("Elemento no Disponible")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.clear()
            element.send_keys(texto)
        except Exception as ex:
            print(str(ex))
            raise

    def clickButton(self, etiqueta, atributo, valor, index):
        driver = self.driver
        try:
            xpath = "(//" + etiqueta + "[@" + atributo + "='" + valor + "'])[" + index + "]"
            super().waitUntilElementIsVisible(xpath)
            element = driver.find_element(By.XPATH, xpath)
            if not super().isDisplayed(element):
                print("Elemento No Desplegado")
            if not super().isEnabled(element):
                print("Elemento no Disponible")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        except Exception as ex:
            print(str(ex))
            raise

    def clickButtonTexto(self, etiqueta, valor, index):
        driver = self.driver
        try:
            xpath = "(//" + etiqueta + "[contains(text(),'" + valor + "')])[" + index + "]"
            super().waitUntilElementIsVisible(xpath)
            element = driver.find_element(By.XPATH, xpath)
            if not super().isDisplayed(element):
                print("Elemento No Desplegado")
            if not super().isEnabled(element):
                print("Elemento no Disponible")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        except Exception as ex:
            print(str(ex))
            raise

    def getText(self, etiqueta, atributo, valor, index):
        driver = self.driver
        try:
            xpath = "(//" + etiqueta + "[@" + atributo + "='" + valor + "'])[" + index + "]"
            super().waitUntilElementIsVisible(xpath)
            element = driver.find_element(By.XPATH, xpath)
            if not super().isDisplayed(element):
                print("Elemento No Desplegado")
            if not super().isEnabled(element):
                print("Elemento no Disponible")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return element.text
        except Exception as ex:
            print(str(ex))
            raise