"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Reverse the given string including space between it
"""

# slicing method
name = input("Enter the name and last name :")
rev_name = name[len(name)::-1] # : staring and 2: is end
print(rev_name)

# using loop
index = len(name)
rev_name1 = []
while index >0:
    rev_name1 += name[index-1]
    index = index-1
print(rev_name1)

# using Join method
reversed= ''.join(reversed(name))
print(reversed)