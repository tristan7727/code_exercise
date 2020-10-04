#coding=utf-8

from config import globalparam


# Captured image will be stored under report/img
def get_img(dr, filename):
    path = globalparam.img_path + '\\' + filename
    dr.take_screenshot(path)

