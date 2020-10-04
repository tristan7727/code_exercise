#coding=utf-8

from time import sleep
from public.common import mytest
from public.pages import XeroLoginPage
from public.pages import XeroDashboardPage
from public.pages import XeroBankAccountsPage
from public.common import datainfo
from public.common import basepage
from public.common import util
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
import json
import random
import re
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class XeroLogin(basepage.Page):

    """
    Page info:
    URL, Username, Password
    """
    url_Login = 'https://login.xero.com/'
    url_Dashboard = 'https://go.xero.com/Dashboard/'
    
    get_data = util.Util_Fun()
    username_ADMIN = get_data.get_cell_vaules(0,1)
    password_ADMIN = get_data.get_cell_vaules(1,1)


    """
    Page Elements info
    """
    username_Login = 'xpath->//*[@id="email"]'
    password_Login = 'xpath->//*[@id="password"]'
    loginButton_Login = 'xpath->//*[@id="submitButton"]'



    """
    Generic functions
    """
    def into_login_page(self):
        """Open Login Page"""
        self.dr.open(self.url_Login)


    def return_title(self):
        """Return the title of page"""
        return self.dr.get_title()


    def do_login(self):
        """Login to Dashboard"""
        self.dr.clear_type(self.username_Login,self.username_ADMIN)
        self.dr.clear_type(self.password_Login,self.password_ADMIN)
        self.dr.click(self.loginButton_Login)
        sleep(5)


    def switch_to_random_ORG(self):
        """Randomly switch to another Organsiation from current one"""
        org_url = self.dr.get_Org_URL()
        self.dr.open(org_url)
