"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 14:20 
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 14:22
* @Title: :Python program to remove item(s) from set 
"""
num_set = set([12, 1, 3, 4, 5])
print("Original set:")
print(num_set)
num_set.remove(12)
print("\nAfter removing the specific element from the said set:")
print(num_set)
num_set.pop()
print("\nAfter removing the first element from the said set:")
print(num_set)