#coding=utf-8

import logging
import time
import os
from config import globalparam

log_path = globalparam.log_path
class Log:
    def __init__(self):
        self.logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def __printconsole(self, level, message):
        # Create a logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # Create a handler, to write log
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        # Create another handler, for console output
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # Define the format of handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # Add handler for logger
        logger.addHandler(fh)
        logger.addHandler(ch)
        # Record one piece of log
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # Close file
        fh.close()

    def debug(self,message):
        self.__printconsole('debug', message)

    def info(self,message):
        self.__printconsole('info', message)

    def warning(self,message):
        self.__printconsole('warning', message)

    def error(self,message):
        self.__printconsole('error', message)
