'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-22 18:20  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-22 18:20
* @Title: Inventory Managment System Using OOPS concept
'''

from InventoryDetails import Inventory_Details
from InventoryManagment import Inventory_Managment
from LoggerHandler import logger

inventory = {}
inv1= Inventory_Details(inventory)
inv2 = Inventory_Managment()

if __name__ == '__main__':
    try:
        while(True):
            value = int(input("1:Add ingredients to inventory managment system\n2:Display all ingeridients and price"
                        "\n3:Calculate the price as per your requirments\n"))
            if value == 1:
                inv1.values_for_inventory()
                inv1.json_details()
            elif value == 2:
                inv2.read_from_json()
            elif value == 3:
                inv2.calculation_of_inevtories()
                inv2.json_details()
    
    except Exception as e:
                logger.error(print("Exception occured",type(e).__name__))
           
                
    