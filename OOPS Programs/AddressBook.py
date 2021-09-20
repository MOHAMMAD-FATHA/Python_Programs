'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-20 01:22  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-20 14:23
* @Title: Address Book System Using OOPS concept
'''

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
                self.a [name_of_addresbook] = {} 

                first_name = input("Enter the first name : ")
                self.a [name_of_addresbook]['First Name'] = first_name

                last_name = input("Enter the last name : ")
                self.a [name_of_addresbook]['Last Name']  = last_name

                address = input("Enter the address of person : ")
                self.a[name_of_addresbook]['Address'] = address

                city = input("Enter the city name : ")
                self.a [name_of_addresbook]['City'] = city

                state_name = input("Enter the State name : ")
                self.a [name_of_addresbook]['State'] = state_name

                zip = input(input("Enter the zip code : ")) 
                self.a [name_of_addresbook]['Zip Code'] = zip

                contact = int(input("Enter the  phone number : "))
                self.a [name_of_addresbook]['Phone Number'] = contact
        except ValueError as e:
            print("Enter the Correct Value")

    def edit_address_book(self):
            name_of_addresbook = input("Enter the name of address book which you want to edit : ")
            attribute = int(input("Attribute to be Updat\n1:First Name\n2:Last Name\n3:Address\n4:City Name\n5:State Name\n6:Zip Code\nContact Number\n"))
            new_value = input("Enter new value : ")
            if attribute == 1:
                self.a [name_of_addresbook]['First Name'] = new_value
            elif attribute == 2:
                self.a [name_of_addresbook]["Last Name"] = new_value
            elif attribute == 3:
                self.a [name_of_addresbook]["Address"] = new_value
            elif attribute == 4:
                self.a [name_of_addresbook]["City"] = new_value
            elif attribute == 5:
                self.a [name_of_addresbook]["State"] = new_value
            elif attribute == 6:
                self.a [name_of_addresbook]["Zip Code"] = new_value
            elif attribute == 7:
                self.a [name_of_addresbook]["Phone Number"] = new_value
            

    def delete_address_book(self):
        name_of_addresbook = input("Enter the name of address book which you want to delete : ")
        del self.a [name_of_addresbook]
    
    def print_address_book(self):
        '''
        Discription :
                        This function is used to display the content of Address_Book dictionary
                        i,e the contact details of the person
        '''
        print(self.a)



    