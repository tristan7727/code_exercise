#coding=utf-8

from public.common import basepage
from time import sleep
from public.common import pyselenium
from datetime import datetime
from public.common import util
from public.common import globalvar

class XeroBankaccounts(basepage.Page):

    """
    Page info
    """
    url_bankAccounts = 'https://go.xero.com/Bank/BankAccounts.aspx'
    title = 'Xero | Find your bank'


    """
    Elements info
    """
    add_bankaccount_button = "xpath->//span[text()='Add Bank Account']"
    option_ANZ = "xpath->//li[text()='ANZ (NZ)']"
    account_name = "css->input[name^='accountname']"
    account_type = "css->input[name^='accounttype']"
    option_creditCard = "xpath->//li[text()='Credit Card']"
    #account_number = "xpath->//input[starts-with(@name,'accountnumber')]"
    account_number = "xpath->//input[starts-with(@name,'accountnumber') and @placeholder = '1234']"
    continue_button = "xpath->//span[text()='Continue']"
    bank_accounts = "xpath->//div[@class = 'bank-header']"
  

    """
    Generic functions
    """

    def check_bank_option(self):
        """ Click 'Add Bank Account' button and then select ANZ (NZ)"""
        self.dr.click(self.add_bankaccount_button)
        availability = ''
        if self.dr.element_exist(self.option_ANZ):
            availability = 'Available'
        else:
            availability = 'ANZ (NZ) bank not available'
        return availability

    def add_bank_details(self):
        """ Add Bank Details like Account name, Bank type, Bank number """
        self.dr.click(self.option_ANZ)
        # grab current timestamp as a random string as the Account name must be unique
        name_str = util.Util_Fun()
        randomStr = name_str.get_Str()                                 
        accountName = 'TestFromTristan'+ randomStr
        globalvar.set_value("ACCOUNTNAME",accountName)
        sleep(2)
        self.dr.clear_type(self.account_name,accountName)
        sleep(2)
        self.dr.click(self.account_type)
        sleep(2)
        self.dr.click(self.option_creditCard)
        sleep(4)
        self.dr.click(self.account_number)
        self.dr.clear_type(self.account_number,'8888')
        sleep(2)
        self.dr.click(self.continue_button)

        self.dr.open(self.url_bankAccounts)
        bank_list = []
        all_banks = self.dr.get_elements(self.bank_accounts)
        added_bank = accountName+'\nXXXX-XXXX-XXXX-8888\n  Manage Account '
        for bank in all_banks:
            bank = bank.text
            bank_list.append(bank)
        result = ''
        if added_bank in all_banks:
            result = 'Passed' 
        else:
            result = 'Failed'
        return result
