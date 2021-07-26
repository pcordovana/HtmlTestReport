import sys
sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())
 
from selenium.webdriver.common.by import By
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.Locators import Locator
 
class PythonSwFundationPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.SF = self.driver.find_element(By.LINK_TEXT, Locator.PSF)
 

    def get_PythonSwFundt(self, driver):
        return self.SF