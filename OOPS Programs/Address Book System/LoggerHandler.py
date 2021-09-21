import logging

logger = logging

# Basic configuration and required format of the file.
logger.basicConfig(filename="F:\.metadata\Python\OOPS Programs\Address Book System\ addressbook.log",
                    level=logging.INFO, format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

logger.basicConfig(filename="F:\.metadata\Python\OOPS Programs\Address Book System\ addressbook.log",
                    level=logging.ERROR, format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineo)d')

                    