# Lo scopo e' il test funzionale del login di yahoo
# L'utente e' gia' registrato 
# Step 1 - Open "https://www.python.org/"
# Step 2 - Locate the Login Button and Sign-In using Credentials
# Step 3 - Check whether the page https://accounts.lambdatest.com/dashboard is displayed
#          and Welcome - Dashboard is shown as the Title of the web page
 
from unittest import result


class Locator(object):
 
#Locators for Python Home Page
    pythonHomePage = "https://www.python.org/"
    searchField = "//*[@id='id-search-field']"
    btnGo ="//*[@id='submit']"
    pythonSwFund ="/html/body/div/div[2]/nav/ul/li[2]/a"
    PSF = "PSF"
    resultSearch ="/html/body/div/div[3]/div/section/form/ul/p"
    resultSearch_1 = ".list-recent-events > p"
   
    yh_email_btn = ".\\_yb_inv65"
    yh_logo = "//img[@alt='LambdaTest']"
    yh_signup = "//a[.='Start Free Testing']"
    yh_login = "//a[.='Log in']"


#Locators for python software fundation Page
    pythonPsfPage ='https://www.python.org/psf-landing/'

#Locators for python documentation Page
    pythonDocPage ='Docs'
    languageSelect = 'language_select'
    spanish = "//option[. = 'Spanish']"


#Locators for python package index Page
    pythonPackIndex ="https://pypi.org/"

 
#Locators for Login Page - https://it.yahoo.com/
    yh_login_user_name = "login-username"
    yh_login_password = "login-passwd"
    yh_login_button = "login-signin"
