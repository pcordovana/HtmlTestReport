'''
Nota: 
Con i seguenti xpath individuati dalla selezione della lingua
//select[@id="language_select"]/option[@value="es"]
//select[@id="language_select"]/option[@value="fr"]
//select[@id="language_select"]/option[@value="ja"]
...
si dovrebbe poter verificare il valore selezionato. Non ci sono riuscito,
funziona per le prime due righe e va in eccezione quando seleziona la 
lingua giapponese

'''


from cgitb import text
from lib2to3.pgen2 import driver
import sys
from xml.sax.xmlreader import Locator

from requests import status_codes
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


xPathOptions = ["//option[. = 'Spanish']", "es", "caricata pagina in lingua spagnola",
                "//option[. = 'French']", "fr", "caricata pagina in lingua francese",
                "//option[. = 'Japanese']", "ja", "caricata pagina in lingua giapponese",
                "//option[. = 'Korean']", "ko", "caricata pagina in lingua Koreana",
                "//option[. = 'Brazilian Portuguese']", "pt-br", "caricata pagina in lingua portoghese",
                "//option[. = 'Simplified Chinese']", "zh-cn", "caricata pagina in lingua cinese semplificato",
                "//option[. = 'Traditional Chinese']", "zh-tw", "caricata pagina in lingua cinese tradizionale",
                "//option[. = 'English']", "en", "caricata pagina in lingua dislessica"]

# legge il file di configurazione dell'applicativo per il formato della data da inserire
# nella riga del log file
cfg = ReadConfig()
outRowFmt = time.strftime(cfg.get_log_date_format())

class test_PythonDocPage(WebDriverSetup, unittest.TestCase, ):
 
    def testDocPage(self):
        driver = self.driver
        driver.get(Locator.pythonHomePage)
        driver.set_page_load_timeout(4)
        
        webPageTitle = "Welcome to Python.org"   

        try:
            if driver.title == webPageTitle:
                print("{} : Web Home Page '{}' caricata con successo".format(outRowFmt, webPageTitle))
                self.assertEqual(driver.title, webPageTitle)
        except Exception as error:
            print(error.message + " {} : Python Web Home Page, caricamento fallito".format(outRowFmt))
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
            print(error.msg +" {} : Python Software Foundation Page, caricamento fallito".format(outRowFmt))
            logging.debug(error.msg  + " Python Software Foundation Page, caricamento fallito")
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

        # torna indietro alla pagina del cinese tradizionale
        driver.back()
        sleep(2)
        lnk = driver.find_element_by_link_text('下載這些說明文件')
        print ("{} : Tornato indietro alla selezione della lingua cinese".format(outRowFmt))

        #fine Caso di test
        print ("{} : Fine metodo testDocPage()".format(outRowFmt))


    def cycleOnLanguages(self, driver):
        for ix in range (0, len(xPathOptions), 3):
            # il secondo ciclo da 0 a 4 serve per evitare problemi di sincronia con la pagina web
            for i in range(4):
                try:
                    run_test = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, xPathOptions[ix])))
                    run_test.click()
                    sleep (1)
                    print ("{} : {}".format(outRowFmt, xPathOptions[ix+2]))
                    lnk = None
                    #una volta selezionato l'elemento dal menu a tendina,
                    # controlla il corretto caricamento con .find_element_by_link_text
                    #<a href="download.html">Descarga esta documentación</a>
                    if ix==0:
                        lnk = driver.find_element_by_link_text('Descarga esta documentación')
                    #<a href="download.html">Téléchargement de ces documentations</a>
                    if ix==3:
                        lnk = driver.find_element_by_link_text('Téléchargement de ces documentations')
                    # <a href="download.html">これらのドキュメントのダウンロード</a>
                    if ix==6:
                        lnk = driver.find_element_by_link_text('これらのドキュメントのダウンロード')
                    #<a href="download.html">이 문서 내려받기</a>
                    if ix==9:
                        lnk = driver.find_element_by_link_text('이 문서 내려받기')
                    #<a href="download.html">Baixar esses documentos</a>
                    if ix==12:
                        lnk = driver.find_element_by_link_text('Baixar esses documentos')
                    #<a href="download.html">下载这些文档</a>
                    if ix==15:
                        lnk = driver.find_element_by_link_text('下载这些文档')
                    #<a href="download.html">下載這些說明文件</a>
                    if ix==18:
                        lnk = driver.find_element_by_link_text('下載這些說明文件')
                    break
                except Exception as e:
                    print("{} : {}".format(outRowFmt, e.msg))
                    #assert genera un fail ed esce dal test
                    #raise genera un error ed esce dal test
                    #assert isinstance(lnk , webdriver.firefox.webelement.FirefoxWebElement)
                    raise e 

if __name__ == '__main__':
    unittest.main()
