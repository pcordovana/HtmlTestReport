import sys
sys.path.append(sys.path[0] + "/....")
 
from selenium.webdriver.common.by import By
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.Locators import Locator

# Attenzione, questa pagina viene richiamata solo dalla HomePage in quanto il campo
# risultato della ricerca è presente solo dopo aver eseguito la ricerca

class PythonResultPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.resultFromSearch = driver.find_element(By.XPATH, Locator.resultSearch)

    def get_resultFromSearch (self):
        return self.resultFromSearch

