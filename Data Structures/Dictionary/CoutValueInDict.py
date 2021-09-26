"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to create a dictionary from a string
            Note: Track the count of the letters from the string.
"""

str1 = input("Enter the string") 
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0)+ 1
print(my_dict)

