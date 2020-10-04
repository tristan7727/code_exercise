#coding=utf-8

import codecs
import os
import xlrd
from config import globalparam

data_path = globalparam.data_path
def get_xls_to_dict(xlsname, sheetname):
	"""
	Save ads a dict after reading excel
	Set the first line as keys, all others data as values
	return [{'title':'1','user':'root'},{'title':'2','user':'xiaoshitou'}]
	"""
	# dataresult = []
	# result = []
	datapath = os.path.join(data_path,xlsname)
	xls1 = xlrd.open_workbook(datapath)
	table = xls1.sheet_by_name(sheetname)
	# for i in range(0,table.nrows):
	# 	dataresult.append(table.row_values(i))
	dataresult = [table.row_values(i) for i in range(0, table.nrows)]
	#convert list to dict
	# for i in range(1,len(dataresult)):
	# 	temp = dict(zip(dataresult[0],dataresult[i]))
	# 	result.append(temp)

	result = [ dict(zip(dataresult[0], dataresult[i])) for i in range(1, len(dataresult))]
	return result

def get_url_data(title):
	"""
	Save as a dict after reading txt file; 
	Convert txt to a dict:
	=>/admin/order/index
	{'title1':'url1','order?':'/admin/order/index'}
	"""
	name = 'urlsource.txt'
	txtpath = os.path.join(data_path,name)
	with codecs.open(txtpath,'r',encoding='utf-8') as f:
		txtcontent = f.readlines()
	txtdict = dict([txt.strip().replace('\ufeff','').split('=>') for txt in txtcontent])
	return txtdict[title]

def get_xls_to_list(excelname, sheetname):
	"""
	Save as a list after reading an excel, only return the first line
	return [1,2,3,4,5]
	"""
	datapath = os.path.join(data_path, excelname)
	excel = xlrd.open_workbook(datapath)
	table = excel.sheet_by_name(sheetname)
	result = [table.row_values(i)[0].strip() for i in range(1,table.nrows)]
	return result

if __name__=='__main__':
    res = get_xls_to_list('addressParse.xlsx','Sheet1')
    res = get_xls_to_dict('admin_single_order.xlsx','ordermsg')
    print(res)


