'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-22 18:20  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-22 18:20
* @Title: Inventory Managment System Using OOPS concept
'''

import json
from LoggerHandler import logger


class Inventory_Details:

    '''
        Description:
            This class is to create the json file and add the details into
            it from the console which can be further used
            
    '''

    def __init__(self,inv):
        self.invent_dict = inv

    def values_for_inventory(self):

        '''
        Description:
            This function is used to Add the ingerdients details which are reuired
            and store that details into the dictionary 
        '''
        try:
            num_of_ingredient = int(input("Enter the number of ingredient :"))
            for i in range(num_of_ingredient):
                ingredient = input("Enter the ingredient : ")
                self.invent_dict [ingredient] = {}

                name = input("Enter the name of ingredient : ")
                self.invent_dict [ingredient]['Name'] = name

                price_per_kg = float(input(f"price per kg of {name} : "))
                self.invent_dict [ingredient]['Price/kg'] = price_per_kg
        except Exception as e:
                logger.error(print("Exception occured ",type(e).__name__))

    def json_details(self):
        '''
        Description:
            This function is use to create json file and store the 
            dictionary of ingredient's details into json form
        '''
        try:
            inventory_object = json.dumps(self.i, indent=2)
            with open("InventoryDetails.json","w+") as inventor_file:
                inventor_file.write(inventory_object)
        except Exception as e:
            logger.error(print("Exception occured ",type(e).__name__))
        finally:
            inventor_file.close()

