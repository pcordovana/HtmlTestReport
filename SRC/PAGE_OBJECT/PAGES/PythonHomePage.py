import sys
sys.path.append(sys.path[0] + "/....")
 
from selenium.webdriver.common.by import By
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.Locators import Locator

 
class PythonHomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.searchField = driver.find_element(By.XPATH, Locator.searchField)
        self.btnGo = driver.find_element(By.XPATH, Locator.btnGo)
        self.SF = self.driver.find_element(By.LINK_TEXT, Locator.PSF)
        self.Doc = self.driver.find_element(By.LINK_TEXT, Locator.pythonDocPage)

    def setPythonSwFundt(self, driver):
        #self.SF = self.driver.find_element(By.LINK_TEXT, "PSF").click()
        return self.SF

    def get_searchField (self):
        return self.searchField

    def get_btnGo (self):
        return self.btnGo

    def setPythonDocPage(self, driver):
        return self.Doc

