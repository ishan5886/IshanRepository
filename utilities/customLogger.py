import logging

class LogGen:

    @staticmethod
    def loggen():
        logger = logging.getLogger()

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter('%(levelname)s:%(message)s')

        file_handler = logging.FileHandler('D:\\Python Programs\\SeleniumPavanSDET\\NopCommerce\\Logs\\automation.log')

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        # logging.basicConfig(filename="D:\\Python Programs\\SeleniumPavanSDET\\NopCommerce\\Logs\\automation.log",
        #                 format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%Y %I:%M:%S %p')
        #
        # logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logger




