
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

class LogManager():
    def __init__(self):
        pass
    def __del__(self):
        pass
logger = logging.getLogger("test1")
logger.basicConfig(filename='finder.log', level=logging.DEBUG, format=LOG_FORMAT)
logger2 = logging.getLogger("test2")
logger2.basicConfig(filename='finder2.log', level=logging.INFO, format=LOG_FORMAT)


if __name__ == "__main__":
    logger.info("heh")
    logger2.info("heh2")