#!/usr/bin/python3
# coding=utf-8
import configparser
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")
projectHomeDir = os.path.dirname(proDir)



class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_base_url(self):
        protocol = self.cf.get("HTTP", "protocol")
        # testing environment
        ip = self.cf.get("HTTP", "ip")
        port = self.cf.get("HTTP", "port")
        base_url = protocol + '://' + ip + ':' + port
        # Generating environment
        # basics = self.cf.get("HTTP", "basics")
        # base_url = protocol + '://' + basics
        return base_url

    def get_excelFields(self):
        A = self.cf.get("EXCEL", "module")
        B = self.cf.get("EXCEL", "api_name")

    def get_email(self, mail_key):
        email_value = self.cf.get("EMAIL", mail_key)
        return email_value

    def get_log_name(self):
        log_name = 'logs'
        try:
            log_name = self.cf.get("LOG_FILE", "log_name")
        except configparser.NoOptionError as error:
            print(error + " Name log file not defined, used default name 'logs'")
        finally:
            return log_name

    def get_log_path(self):
        #imposta il default value per il path
        path=os.getcwd()
        log_path = os.chdir(os.path.dirname(os.path.abspath(__file__)))
        try:
            log_path = self.cf.get("LOG_FILE", "log_path")
        except configparser.NoOptionError as error:
            print(error + " Path log file not defined, used current path {}".format(os.chdir(os.path.dirname(os.path.abspath(__file__)))))
        finally:
            return log_path

    def get_log_level(self):
        log_level = 'INFO'
        try:
            log_level = self.cf.get("LOG_FILE", "log_level")
        except configparser.NoOptionError as error:
            print(error + " log level not defined, default level INFO is setting")
        finally:
            return log_level

    def get_log_level_selenium(self):
        log_level = 'INFO'
        try:
            log_level = self.cf.get("LOG_FILE", "log_level_selenium")
        except configparser.NoOptionError as error:
            print(error + " log level not defined, default level INFO is setting")
        finally:
            return log_level


    def get_log_date_format(self):
        #log_date_format = '%d-%m-%Y %H-%M-%S'
        log_date_format =""
        try:
            log_date_format = self.cf.get("LOG_FILE", "log_date_format")
        except configparser.NoOptionError as error:
            print(error + " log date format not defined, used dd-mm-YY hh:mm:ss format")
        finally:
            return log_date_format

    def get_log_row_format(self):
        log_row_format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
        try:
            log_row_format = self.cf.get("LOG_FILE", "log_row_format")
        except configparser.NoOptionError as error:
            print(error + " log date format not defined, used dd-mm-YY hh:mm:ss format")
        finally:
            return log_row_format

    def get_report_name(self):
        report_name = 'report'
        try:
            report_name = self.cf.get("REPORT_FILE", "report_name")
        except configparser.NoOptionError as error:
            print(error + " Name report file not defined, used default name 'report'")
        finally:
            return report_name

    def get_report_path(self):
        report_path =''
        try:
            report_path = projectHomeDir + os.sep + self.cf.get("REPORT_FILE", "report_path")
        except configparser.NoOptionError as error:
            print(error + " Path report file not defined, used current path {}".format(os.chdir(os.path.dirname(os.path.abspath(__file__)))))
        finally:
            return report_path

    def get_report_dir(self):
        report_dir = ''
        try:
            report_dir = self.cf.get("REPORT_FILE", "report_dir")
        except configparser.NoOptionError as error:
            print(error + " Directory name not defined, used REPORTS as default")
        finally:
            return report_dir


'''
uso :

if __name__ == '__main__':
    pippo = ReadConfig()
    print (pippo.get_base_url())
    asdf = pippo.get_email("is_send")

if  asdf == 'yes':
    print ("The test report has been emailed!")
else:
    print("Test reports do not send e-mail!")

''' 