"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 14:16 
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 14:17 
* @Title: :Python program to remove an item from a set if it is present in the set 
"""

#Create a new set
num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
print(num_set)
print("\nRemove 22 from the said set:")
num_set.discard(22)
print(num_set)
print("\nRemove 2 from the said set:")
num_set.discard(2)
print(num_set)