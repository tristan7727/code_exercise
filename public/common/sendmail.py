#coding:utf-8

import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from public.common.log import Log
from config import globalparam

# Path of test report
reportPath = globalparam.report_path
logger = Log()
# Configure receiver
recvaddress = ['RECEIVER_EMAILADDRESS@GMAIL.COM']

# Account info of sender
sendaddr_name = 'SENDER_EMAILADDRESS@GMAIL.COM'
sendaddr_pswd = 'YOUR EMAIL PASSWORD'

class SendMail:
	def __init__(self,recver=None):
		"""Recipient list：list or tuple"""
		if recver is None:
			self.sendTo = recvaddress
		else:
			self.sendTo = recver

	def __get_report(self):
		"""To get the latest test report"""
		dirs = os.listdir(reportPath)
		dirs.sort()
		newreportname = dirs[-1]
		print('The new report name: {0}'.format(newreportname))
		return newreportname

	def __take_messages(self):
		"""Generate Email contents, html and attachment"""
		newreport = self.__get_report()
		self.msg = MIMEMultipart()
		self.msg['Subject'] = 'Test Report Subject'
		self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

		with open(os.path.join(reportPath,newreport), 'rb') as f:
			mailbody = f.read()
		html = MIMEText(mailbody,_subtype='html',_charset='utf-8')
		self.msg.attach(html)
		
		# html attachment
		att1 = MIMEText(mailbody, 'base64', 'gb2312')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
		self.msg.attach(att1)

	def send(self):
		"""Send Email"""
		self.__take_messages()
		self.msg['from'] = sendaddr_name
		try:
			smtp = smtplib.SMTP('smtp.126.com')
			smtp.login(sendaddr_name,sendaddr_pswd)
			smtp.sendmail(self.msg['from'], self.sendTo,self.msg.as_string())
			smtp.close()
			logger.info("Email sent successfully")
		except Exception:
			logger.error('Email sent failed')
			raise

if __name__ == '__main__':
	sendMail = SendMail()
	sendMail.send()

        
