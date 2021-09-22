'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-22 18:20  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-22 18:20
* @Title: Inventory Managment System Using OOPS concept
'''
import json
from LoggerHandler import logger

class Inventory_Managment:
    '''
    Description:
        This class is to read the json file which was created in Inventory Details
        and use those details for requirements and calculation 
            
    '''
    def __init__(self):
        pass

    def read_from_json(self):

        '''
        Description:
            This function is used to open json file which contains the ingredients
            details and store it into dictionary for further usage in calculation
        '''
        try:
            with open ("F:\.metadata\Python\OOPS Programs\Inventory Managment System\InventoryDetails.json","r") as inventory_file:

                self.inventor_dict = json.load(inventory_file)
                print(self.inventor_dict)
                print(type(self.inventor_dict))
                
        except Exception as e:
            logger.error(print("Exception occured ",type(e).__name__))

    def calculation_of_inevtories(self):
        '''
        Description:
            This function is used to fetch the required data for calculation from the above
            created dictionary from json file 
        '''
        try:
            self.sys_inventor = {} #Empty dictionary to store the result
            num_of_ingredient = int(input("Enter how many ingredients details and cost you want to calculate : "))
            
            for i in range(num_of_ingredient):
            
                name_of_ingredient = input("Enter the name of ingredient you want : ")
                req_ingredient = int(input(f"Enter the how many kg of {name_of_ingredient} want : "))
            
                if self.inventor_dict.get(name_of_ingredient) is not None:
                    x = self.inventor_dict [name_of_ingredient]['Price/kg']
                    total = "{:.2f}".format(req_ingredient * (self.inventor_dict [name_of_ingredient]['Price/kg']))
                    # Above line is just to convert the answer into 2 decimel ponits
                    print(f"Total cost requirs for {req_ingredient}kg {name_of_ingredient} is :",total)
                    y = f'Price for {req_ingredient} {name_of_ingredient}'
                    self.sys_inventor [name_of_ingredient] = {}
            
                    for k,v in self.inventor_dict [name_of_ingredient].items():
                        self.sys_inventor [name_of_ingredient] [k]=v

                    self.sys_inventor [name_of_ingredient] [y] = total
                    print(self.sys_inventor)

        except Exception as e:
            logger.error(print("Exception occured ",type(e).__name__))
               

    def json_details(self):
        '''
        Description:
            This function is used to store the all the data with calculation into another
            json file which contains the details and as we as requirements calculations and
            details
        '''
        try:
            inventory_object = json.dumps(self.sys_inventor, indent=2)
            with open("InventoryManagment.json","w+") as inventor_file:
                    inventor_file.write(inventory_object)
        except Exception as e:
            logger.error(print("Exception occured ",type(e).__name__))
        finally:
            inventor_file.close()  
    