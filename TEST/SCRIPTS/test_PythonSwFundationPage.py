import sys
from xml.sax.xmlreader import Locator
sys.path.append(sys.path[0] + "/...")
 
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.TEST_BASE.WebDriverSetup import WebDriverSetup
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.TEST_BASE.ElementsDescriptor import ElementsDescriptor
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.PAGES.PythonHomePage import PythonHomePage
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.PAGES.PythonSwFundationPage import PythonSwFundationPage
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.Locators import Locator
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.CONFIG.readConfig import ReadConfig
import unittest
from selenium import webdriver
from time import sleep
import logging
import os
import time

# legge il file di configurazione dell'applicativo per il formato della data da inserire
# nella riga del log file
cfg = ReadConfig()
outRowFmt = time.strftime(cfg.get_log_date_format())


class test_PythonSwFundationPage(WebDriverSetup, unittest.TestCase):
 
    def testSwFundationPage(self):
        driver = self.driver
        self.driver.get(Locator.pythonHomePage)
        self.driver.set_page_load_timeout(4)

        webPageTitle = "Welcome to Python.org"
        
        #localizza e cambia la directory dello script corrente con 
        # os.getcwd() e os.chdir() per salvare il file di log
        path=os.getcwd()
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        logger = logging.getLogger('logger_Admin')
        print("{} : Attivato logger in modalita' logger_Admin".format(outRowFmt))

        try:
            if driver.title == webPageTitle:
                print("{} : Web Home Page '{}' caricata con successo".format(outRowFmt, webPageTitle))
                self.assertEqual(driver.title, webPageTitle)
                logger.info("Web Home Page '{}' caricata con successo".format(webPageTitle))
        except Exception as error:
            print(error + " {} : Python Web Home Page, caricamento fallito".format(outRowFmt))
            logging.debug(error + " Python Web Home Page, caricamento fallito")
 
        # Crea una istanza della classe per usare i suoi metodi
        swFundationPage = PythonSwFundationPage(driver)

        # seleziona la Software Fundation Page
        swFundationPage.get_PythonSwFundt(driver).click()
        logger.info('Selezionata SFP Page')
        print ("{} : selezionata la pagina Software Foundation".format(outRowFmt))
        sleep(2)

        webPageTitle = "Python Software Foundation"
        try:
            if driver.title == webPageTitle:
                logger.info("Web Home Page '{}' caricata con successo".format(webPageTitle))
                print("{} : Web Page '{}' caricata con successo".format(outRowFmt , webPageTitle))
                self.assertEqual(driver.title, webPageTitle)
        except Exception as error:
            print(error+" {} : Python Software Foundation Page, caricamento fallito".format(outRowFmt))
            logging.debug(error + " Python Software Foundation Page, caricamento fallito")
        finally:
            print("{} : Fine metodo testSwFundationPage()".format(outRowFmt))
        sleep(2)
 
if __name__ == '__main__':
    unittest.main()
