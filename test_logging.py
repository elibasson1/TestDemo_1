import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)  # __import__()  --> for test case name
    fileHandler = logging.FileHandler('logfile.log') # create file to save all log file
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # file handler object

    logger.setLevel(logging.INFO)
    logger.debug("A debug message is execute")
    logger.info("Information statement")
    logger.warning("something is in warning mode")
    logger.error("A major error has happend")
    logger.critical("Critical issue")