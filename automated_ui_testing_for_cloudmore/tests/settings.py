from pyunitreport import HTMLTestRunner
import unittest
import os
import utils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WEBSITE_URL = "https://web.cloudmore.com/"
# PS. on ubuntu or mac it will work, 
# but if you are using Windows download and add geckodriver from selenium website and add local link here.
# For Example: "C:\\Program Files\\geckodriver.exe"
WEBDRIVER_PATH = "./webdriver/geckodriver" 
MENU_LINKS = utils.get_menu_links(WEBSITE_URL)