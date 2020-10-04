#coding=utf-8

from time import sleep
from public.common import mytest
from public.pages import XeroLoginPage
from public.pages import XeroDashboardPage
from public.pages import XeroBankAccountsPage
from public.pages import XeroChartOfAccountsPage
from public.common import datainfo
from public.common import pyselenium


class SanityTest_Xero(mytest.MyTest):
    """UAT"""


    def test_add_bank_account_info(self):
        """ Login page """
        #STEP1: go to login page and check the page title
        login_page = XeroLoginPage.XeroLogin(self.dr)
        login_page.into_login_page()
        title_login = login_page.return_title()
        #CheckPoint1: to check title of the Login page
        self.assertIn('Login | Xero Accounting Software',title_login,"CheckPoint1: Failed to load Login page")
    

        """ Dashboard page """
        #STEP2: login, check title of Dashboard after switching to another Organ
        login_page.do_login()
        login_page.switch_to_random_ORG()
        title = login_page.return_title()
        #CheckPoint2: to check the title of Dashboard page
        self.assertIn("Xero | Dashboard",title,"CheckPoint2: Failed to load Dashboard after switching to another Organsiation")


        """ Bank Accounts page """
        #STEP3: go to Bank Account page and check the title
        dashboard = XeroDashboardPage.XeroDashboard(self.dr)
        dashboard.switch_to_bankaccount_page()
        title_bankaccount = login_page.return_title()
        #CheckPoint3: to check the title of Bank Accounts page
        self.assertIn("Xero | Bank accounts",title_bankaccount,"CheckPoint3: Failed to load Bank accounts page")
        

        """ ANZ (NZ) bank availability """
        #STEP4: Add bank account and check whether ANZ (NZ) bank is available
        bankAccount = XeroBankAccountsPage.XeroBankaccounts(self.dr)
        result_ANZavailability = bankAccount.check_bank_option()
        #CheckPoint4: to check whether the ANZ (NZ) bank is available
        self.assertIn('Available',result_ANZavailability,"CheckPoint4: Failed to add ANZ (NZ) bank as the option is not available")
        

        """ New Bank Account """
        #STEP5: Add bank account and check whether bank account has been added successfully
        bankAccount = XeroBankAccountsPage.XeroBankaccounts(self.dr)
        result_bankStatus = bankAccount.add_bank_details()
        #CheckPoint5: to check whether bank account has been added successfully
        self.assertIn('Failed', result_bankStatus,"CheckPoint5: Failed to add Bank account")


        """ TearDown """
        #STEP6: Clear newly added bank account info from this account
        chartAccounts = XeroChartOfAccountsPage.XeroChartAccount(self.dr)
        result_bankRemoval = chartAccounts.delete_bankAccount()
        #CheckPoint6: to check whether bank account has been deleted successfully
        self.assertIn('Bank Account has been deleted successfully', result_bankRemoval,"CheckPoint6: Failed to Delete Bank account")

        