#coding=utf-8

import os
from public.common.readconfig import ReadConfig

# Ready configuration file
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# Set project parameter
prj_path = read_config.getValue('projectConfig','project_path')
# Path of log
log_path = os.path.join(prj_path, 'report', 'log')
# Path of screenshot
img_path = os.path.join(prj_path, 'report', 'image')
# Path of test report
report_path = os.path.join(prj_path, 'report', 'testreport')
# Default browser
browser = 'chrome'

# Path of test data
data_path = os.path.join(prj_path, 'data', 'testdata')
