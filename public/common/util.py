import xlrd
import xlwt
from xlutils.copy import copy
from time import gmtime, strftime
from datetime import datetime, timedelta
import sys
import os
from public.common import globalvar
#sys.path.append(r"../../")

class Util_Fun:

    def __init__(self, file_name=None,sheet_id=NotImplementedError):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = os.path.join(globalvar.get_value("ROOT_DIR"), 'data/testdata/data_info.xlsx')
            self.sheet_id = 0
        self.data = self.get_data()

    #to get contents of certain sheet in excel
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #to get numbers of rows
    def get_rows(self):
        tables = self.data
        return tables.nrows

    #to get the value of certain cell
    def get_cell_vaules(self,row,col):
        tables = self.data
        return tables.cell_value(row,col)
    
    def write_value(self,row,col,value):
        '''
        write into excel
        '''
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    def get_Str(self):
        """
        To use the current timestamp as a random string for Bank Account name
        
        Usage:
        get_currentTime(self)
        """
        random_Str = datetime.now().strftime('%Y%m%d%H%M%S')
        return random_Str



if __name__ == '__main__':
    opers = Util_Fun()
    opers.get_data().nrows
    opers.get_rows()
    print(opers.get_cell_vaules(3,0))
