'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-20 01:22  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-21 17:15
* @Title: Address Book System Using OOPS concept
'''

from LoggerHandler import logger
from Validation import Validation
import json

class AddressBook:
    def __init__(self,Address) :
            self.a = Address
            
    
    def create_address_book(self):

        '''
        Discription :
                        This function is to create a Address Book and store it 
                        into the dictionary. 
        '''
        try:
            num_of_cont = int(input("Enter the number of contacts you want to add :"))
   
            for i in range(num_of_cont): # Used to count the number of persons to add in address book
                name_of_addresbook = input("Enter the name of address book : ")
                if self.a.get(name_of_addresbook) is not None: 
                    # Address book name should be unique so it check address book name is already exist or not
                    logger.error("Entred Address book is already exist : ")
                    break
                else:
                    
                    self.a [name_of_addresbook] = {} 

                    print("Enter your first name : ")
                    first_name = Validation.name_validation()
                    self.a [name_of_addresbook]['First Name'] = first_name

                    print("Enter your last name : ")
                    last_name = Validation.name_validation()
                    self.a [name_of_addresbook]['Last Name']  = last_name

                    print("Enter your Address : ")
                    address = input()
                    self.a[name_of_addresbook]['Address'] = address

                    print("Enter your city name : ")
                    city = Validation.name_validation()
                    self.a [name_of_addresbook]['City'] = city

                    print("Enter your state name : ")
                    state_name = Validation.name_validation()
                    self.a [name_of_addresbook]['State'] = state_name

                    zip = Validation.validate_zip() 
                    self.a [name_of_addresbook]['Zip Code'] = zip

                    contact = Validation.phone_number_validation()
                    self.a [name_of_addresbook]['Phone Number'] = contact
        except ValueError:
            print("Enter the Correct Value")

    def edit_address_book(self):
        '''
        Description:
            This function edit the contact details of person from Address Book.
            Here we edit details using the name of Address Book name. 
        '''
        try:
            name_of_addresbook = input("Enter the name of address book which you want to edit : ")
            attribute = int(input("Attribute to be Updat\n1:First Name\n2:Last Name\n3:Address\n4:City Name\n5:State Name\n6:Zip Code\nContact Number\n"))
            new_value = input("Enter new value : ")
            if attribute == 1:
                new_value = Validation.name_validation()
                self.a [name_of_addresbook]['First Name'] = new_value
            elif attribute == 2:
                new_value = Validation.name_validation()
                self.a [name_of_addresbook]["Last Name"] = new_value
            elif attribute == 3:
                new_value = input("Enter the address : ")
                self.a [name_of_addresbook]["Address"] = new_value
            elif attribute == 4:
                new_value = Validation.name_validation()
                self.a [name_of_addresbook]["City"] = new_value
            elif attribute == 5:
                new_value = Validation.name_validation()
                self.a [name_of_addresbook]["State"] = new_value
            elif attribute == 6:
                new_value = Validation.validate_zip()
                self.a [name_of_addresbook]["Zip Code"] = new_value
            elif attribute == 7:
                new_value = Validation.phone_number_validation()
                self.a [name_of_addresbook]["Phone Number"] = new_value
        except Exception as e:
            logger.error("Kindly enter valid info : ",e)
            self.edit_address_book()
            
    def delete_address_book(self):
        '''
        Description:
            This function delete the contact details of person from Address Book.
            Here we delete details using the name of Address Book name. 
        '''
        try:
            name_of_addresbook = input("Enter the name of address book which you want to delete : ")
            del self.a [name_of_addresbook]
        except ValueError:
            logger.error("Kindly Provide valid info : ")
            self.delete_address_book()
    
    def write_in_json(self):
        try:
            json_object = json.dumps(self.a, indent=2)
            with open("F:\.metadata\Python\OOPS Programs\Address Book System\ addressbook.json","w+") as addressfile:
                addressfile.write(json_object)
                logger.info("File created and saved successfully")
        except Exception as e:
            logger.error("Exception occured : ",type(e).__name__)
        finally:
            addressfile.close()
        

    def read_from_json(self):
        try:
            with open ("F:\.metadata\Python\OOPS Programs\Address Book System\ addressbook.json","r") as jsonfile:
                json_object = json.load(jsonfile)
        except Exception as e:
            logger.error("File doesnt exist")


    def print_address_book(self):
        '''
        Discription :
                        This function is used to display the content of Address_Book dictionary
                        i,e the contact details of the person
        '''
        print(self.a)



    