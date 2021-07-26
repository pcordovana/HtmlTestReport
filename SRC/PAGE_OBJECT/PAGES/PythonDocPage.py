import sys
sys.path.append(sys.path[0] + "/....")

 
from selenium.webdriver.common.by import By
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.Locators import Locator
 
class PythonDocPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.LanguageSelect = self.driver.find_element(By.ID, Locator.languageSelect)
        self.DropDownLanguage = self.driver.find_element(By.ID, Locator.languageSelect)

    def get_PythonDocPage(self, driver):
        return self.Doc
    
    def get_LanguageSelect(self, driver):
        return self.LanguageSelect

    def get_DropDownLanguage(self, driver):
        return self.DropDownLanguage

    def get_Mistero (self, driver):
        return self.Mistero