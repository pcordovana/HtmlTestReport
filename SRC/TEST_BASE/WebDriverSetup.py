import unittest
from selenium import webdriver
import time
from time import sleep
import warnings
import urllib3
 
class WebDriverSetup():

    #il decoratore ci permette di impostare i valori a livello di classe
    # in modo da poter essere condiviso tra i metodi del test
    @classmethod
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
 
    @classmethod
    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()