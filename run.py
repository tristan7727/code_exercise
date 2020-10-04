#coding=utf-8

import unittest
import HTMLTestRunner
import time
import os
#from config import globalparam
from public.common import globalvar
from public.common import sendmail

def run():
    
    globalvar._init()  # Initialise global variable
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    globalvar.set_value("ROOT_DIR", ROOT_DIR) 
    test_dir = os.path.join(ROOT_DIR, 'testcase') 
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='TC*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    #reportname = globalparam.report_path + '//' + 'TestResult-' + now + '.html'
    reportname =  ROOT_DIR + '//' + 'Report/' + 'TestResult-' + now + '.html'
    ROOT_DIR
    ROOT_DIR
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='Coding Exercise - Xero',
            description='Coding Exercise to add ANZ (NZ) Bank Account for any Organsiation'
        )
        runner.run(suite)
    time.sleep(3)
    # Send Email
    #mail = sendmail.SendMail()
    #mail.send()

if __name__=='__main__':
    run()