"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: : Print out a set containing all the colors from color_list_1 which
are not present in color_list_2.
"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(type(color_list_1,))
print(type(color_list_2))

print("Colours of colour list 1")
print(color_list_1)
print("Colours of colour list 2")
print(color_list_2)

print("Differnt colour present in color_list_1 ar :")
#This is to check what all colours are present set which are not there is set 2
print(color_list_1.difference(color_list_2)) 
#This is will minus the content of set 1 from the set 2
print(color_list_1 - color_list_2)