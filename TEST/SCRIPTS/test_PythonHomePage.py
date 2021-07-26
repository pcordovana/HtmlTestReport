import sys
from xml.sax.xmlreader import Locator
sys.path.append(sys.path[0] + "/...")
 
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.TEST_BASE.WebDriverSetup import WebDriverSetup
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.TEST_BASE.ElementsDescriptor import ElementsDescriptor
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.PAGES.PythonHomePage import PythonHomePage
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.PAGES.PythonResultPage import PythonResultPage
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.Locators import Locator
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.CONFIG.readConfig import ReadConfig
import unittest
from selenium import webdriver
from time import sleep
import time

# legge il file di configurazione dell'applicativo per il formato della data da inserire
# nella riga del log file
cfg = ReadConfig()
outRowFmt = time.strftime(cfg.get_log_date_format())

class test_PythonHomePage(WebDriverSetup, unittest.TestCase):
 
    def testHomePage(self):
        driver = self.driver
        self.driver.get(Locator.pythonHomePage)
        self.driver.set_page_load_timeout(4)
 
        webPageTitle = "Welcome to Python.org"
 
        try:
            if driver.title == webPageTitle:
                print("{} : Web Home Page '{}' caricata con successo".format(outRowFmt, webPageTitle))
                self.assertEqual(driver.title, webPageTitle)
        except Exception as error:
            print(error+" {} : Python Web Page, caricamento fallito".format(outRowFmt))
 
        # Crea una istanza della classe per usare i suoi metodi
        homePage = PythonHomePage(driver)
        print("{} : Crea una istanza della classe PythonHomePage".format(outRowFmt))

        #cerca il campo della ricerca, si posiziona con un click e lo pulisce
        homePage.get_searchField().click()
        homePage.get_searchField().clear()
        print("{} : Posizionamento nel campo ricerca della PythonHomePage".format(outRowFmt))

        # inserisce un contenuto da cercare nel campo di ricerca
        homePage.get_searchField().send_keys("Akusinusi")

        # simula click tasto GO per la ricerca
        homePage.btnGo.click()
        print("{} : Ricerca della parola Akusinusi (inesistente)".format(outRowFmt))

        # controlla il risultato della ricerca, instanzia la classe resultPage per il controllo del risultato
        # i due assert sono equivalenti
        driver.implicitly_wait(5)
        resultPage = PythonResultPage(driver)
        result = resultPage.get_resultFromSearch()
        print ("{} : Ricerca di Akusinusi: {}".format(outRowFmt, result.text))
        assert "No results found." in result.text
        assert "No results found." in driver.page_source
   
        print("{} : Fine metodo testHomePage()".format(outRowFmt))

        sleep(2)
 
if __name__ == '__main__':
    unittest.main()