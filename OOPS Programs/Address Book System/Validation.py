'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-20 01:22  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-21 17:15
* @Title: Address Book System Using OOPS concept
'''

from LoggerHandler import logger
import re

class Validation: 

    '''
    Description:
            This class is used for validation of the user inputs using Regex
    '''

    def name_validation():

        '''
        Description:
        This class holds the methods to validate all the details entered by User.
        Regex is used to validate the details.
        '''

        while(True):
            try:
                first_name = input("")
                if re.match("^[A-Z]{1}[a-z]{2,}$",first_name):
                    logger.info("Execited")
                    return first_name
                else:
                    logger.error(print("Please enter valid name "))
            except ValueError:
                logger.error("Enter valid  Name")

    def phone_number_validation():

        '''
        Description:
            This function is to validate mobile number of the person.
            Mobile number should start with country code 91 and should have 10 digits.
        Returns: Valid mobile number.
            
        '''
        while(True):
            try:
                phone_number = input("Enter the Mobile number : ")
                if re.match("^(91)[0-9]{10}$",phone_number):
                    logger.info("Executed")
                    return phone_number
                else:
                    logger.error("Enter the Valid Phone number")
            except ValueError:
                logger.error("Enter Valid phone number")

    def validate_zip():
        '''
        Description:
            This function is to validate entered Zip code of the person's city.
        Returns: Valid zip code.
         
        '''
        while(True):
            try:
                while True:
                    zip = input("Enter your zip: ")
                    if re.match("^[1-9]{1}[0-9]{5}$", zip):
                        logger.info("Executed")
                        return zip
                    else:
                        logger.error("Invalid zip")
            except ValueError:
                logger.error("Invalid zip")