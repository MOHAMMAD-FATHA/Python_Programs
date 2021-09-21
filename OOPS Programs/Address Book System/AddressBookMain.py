'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-20 01:22  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-21 17:15
* @Title: Address Book System Using OOPS concept
'''
from AddressBook import AddressBook
Address_Book = {}
addressbook = AddressBook(Address_Book)
from LoggerHandler import logger

if __name__ == '__main__':
    try:
        while(True):
            print("1:Add contacts in to Address Book\n2:Edit the contacts in Address Book\n3:Delete the contacts from address book\n4:Display Address Book\n5:Write Address Book in JSON\n6:Read Address Book from JSON\n7:Exit\n")
            option = int(input())
            if option == 1 :
                addressbook.create_address_book()
            elif option == 2:
                addressbook.edit_address_book()
            elif option == 3:
                addressbook.delete_address_book()
            elif option == 4:
                addressbook.print_address_book()
            elif option == 5:
                addressbook.write_in_json()
            elif option == 6:
                addressbook.read_from_json()
            else:
                break
    except ValueError:
        logger.error("Invalid Input")
    
    

    