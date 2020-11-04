import inspect
import logging


class BaseClass:

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)  # __import__()  --> for test case name
        fileHandler = logging.FileHandler('logfile.log')  # create file to save all log file
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # file handler object
        logger.setLevel(logging.DEBUG)

        return logger
