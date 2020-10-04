#coding=utf-8

from public.common import basepage
from time import sleep
from public.common import pyselenium
from datetime import datetime
from public.common import globalvar

class XeroChartAccount(basepage.Page):

    """
    Page info
    """
    url_chart = 'https://go.xero.com/GeneralLedger/ChartOfAccounts.aspx'
    title_ChartsAccounts = 'Xero | Chart of accounts'


    """
    Elements info
    """
    search_box = "xpath->//*[@name='SearchTermsText']"
    search_button = "xpath->//span[text()='Search']/.."
    selectAll_checkbox ="xpath->//input[@type='checkbox' and @title='Select all accounts']"
    delete_button = "xpath->//a[text()='Delete']"
    popupOK_button = "xpath->//a[@id='popupOK']"

    bank_tableBody = "xpath->//table[@id='chartOfAccounts']/tbody/tr"

    
    """
    Generic functions
    """
    def delete_bankAccount(self):
        """ Select bank, delete and check again"""
        self.dr.open(self.url_chart)
        keywords = globalvar.get_value("ACCOUNTNAME")
        self.dr.clear_type(self.search_box,keywords)
        self.dr.click(self.search_button)
        self.dr.click(self.selectAll_checkbox)
        self.dr.click(self.delete_button)
        self.dr.click(self.popupOK_button)

        self.dr.clear_type(self.search_box,keywords)
        self.dr.click(self.search_button)
        bankAccount_status = ''
        if self.dr.element_not_exist(self.bank_tableBody):
            bankAccount_status = 'Bank Account has been deleted successfully'
        else:
            bankAccount_status = 'Bank Account Not deleted successfully'
        return bankAccount_status
