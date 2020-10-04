#coding=utf-8

from public.common import basepage
from time import sleep
from public.common import pyselenium
from datetime import datetime

class XeroDashboard(basepage.Page):

    """
    Page info
    """
    title_BankAccountPage = 'Xero | Bank accounts'


    """
    Elements info
    """

    url_bankAccounts = 'https://go.xero.com/Bank/BankAccounts.aspx'
    #accounting_tab = 'name->navigation-menu/accounting'
    #bankaccount_menu = 'partial_link_text->Bank'


    """
    Generic functions
    """

    """Dashboard_SysADMIN"""
    def switch_to_bankaccount_page(self):
        """ Switch to Bank Account page from Dashboard """
        sleep(2)
        self.dr.open(self.url_bankAccounts)
        sleep(2)

