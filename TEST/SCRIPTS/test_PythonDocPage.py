import sys
from xml.sax.xmlreader import Locator
sys.path.append(sys.path[0] + "/...")
 
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.TEST_BASE.WebDriverSetup import WebDriverSetup
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.TEST_BASE.ElementsDescriptor import ElementsDescriptor
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.PAGES.PythonHomePage import PythonHomePage
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.PAGES.PythonDocPage import PythonDocPage
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.SRC.PAGE_OBJECT.Locators import Locator
from PAGE_OBJECT_MODEL.PROJECT_PAGE_PYTHON.CONFIG.readConfig import ReadConfig
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import logging
import os
import time

xPathOptions = ["//option[. = 'Spanish']", "caricata pagina in lingua spagnola",
                "//option[. = 'French']", "caricata pagina in lingua francese",
                "//option[. = 'Japanese']", "caricata pagina in lingua giapponese",
                "//option[. = 'Korean']", "caricata pagina in lingua Koreana",
                "//option[. = 'Brazilian Portuguese']", "caricata pagina in lingua portoghese",
                "//option[. = 'Simplified Chinese']", "caricata pagina in lingua cinese semplificato",
                "//option[. = 'Traditional Chinese']", "caricata pagina in lingua cinese tradizionale",
                "//option[. = 'English']", "caricata pagina in lingua dislessica"]

# legge il file di configurazione dell'applicativo per il formato della data da inserire
# nella riga del log file
cfg = ReadConfig()
outRowFmt = time.strftime(cfg.get_log_date_format())

class test_PythonDocPage(WebDriverSetup, unittest.TestCase, ):
 
    def testDocPage(self):
        driver = self.driver
        self.driver.get(Locator.pythonHomePage)
        self.driver.set_page_load_timeout(4)
        
        webPageTitle = "Welcome to Python.org"   

        try:
            if driver.title == webPageTitle:
                print("{} : Web Home Page '{}' caricata con successo".format(outRowFmt, webPageTitle))
                self.assertEqual(driver.title, webPageTitle)
        except Exception as error:
            print(error + " {} : Python Web Home Page, caricamento fallito".format(outRowFmt))
        sleep(2)

        # Crea una istanza della classe per usare i suoi metodi
        action = ActionChains(driver)
        homePage = PythonHomePage(driver)
        firstLevelMenu = homePage.setPythonDocPage(driver)
        action.move_to_element(firstLevelMenu).perform()

        print("{} : Crea una istanza della classe PythonHomePage".format(outRowFmt))
        homePage.setPythonDocPage(driver).click()
        print("{} : Accede alla pagina Document".format(outRowFmt))
        
        sleep(2)
        # Crea una istanza della classe PythonDocPage per usare i suoi metodi
        swDocPage = PythonDocPage(driver)
        print ("{} : Crea una istanza della classe PythonDocPage".format(outRowFmt))

        webPageTitle = "3.9.6 Documentation"
        try:
            if driver.title == webPageTitle:
                print("{} : Web Page '{}' caricata con successo".format(outRowFmt, webPageTitle))
                self.assertEqual(driver.title, webPageTitle)
            else:
                print("{} : Web Page '{}' NON caricata".format(webPageTitle, outRowFmt))
                print("{} : atteso {}   ottenuto {}".format(webPageTitle, driver.title, outRowFmt))             
                raise NameError('Errore di caricamento pagina')

        except Exception as error:
            print(error+" {} : Python Software Foundation Page, caricamento fallito".format(outRowFmt))
            logging.debug(error + " Python Software Foundation Page, caricamento fallito")
        finally:
            print("{} : Controllo caricamento pagina Documentation effettuato".format(outRowFmt))
        sleep(2)

        # A questo punto ha caricato correttamente la documentation Page
        # seleziona il menu a tendina
        action = ActionChains(driver)
        firstLevelMenu = swDocPage.get_LanguageSelect(driver)
        action.move_to_element(firstLevelMenu).perform()
        swDocPage.get_LanguageSelect(driver).click()
        sleep(1)

        #cicla su tutte le possibilita' del menu a tendina e
        # carica automaticamente le rispettive pagine
        self.cycleOnLanguages(driver)

        print ("{} : Fine metodo testDocPage()".format(outRowFmt))


    def cycleOnLanguages(self, driver):
        for ix in range (0, len(xPathOptions), 2):
            for i in range(4):
                try:
                    run_test = WebDriverWait(driver, 120).until( \
                    EC.presence_of_element_located((By.XPATH, xPathOptions[ix])))
                    run_test.click()
                    print ("{} : {}".format(outRowFmt, xPathOptions[ix+1]))
                    sleep (2)
                    break
                except Exception as e:
                    raise e 
 
if __name__ == '__main__':
    unittest.main()
