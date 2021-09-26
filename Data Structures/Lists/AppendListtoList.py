"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 00:15
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 00:20 
* @Title: :Python program to append a list to the second list.
"""

l1 = [1,2,2,3,4]
l2 = [5,6,7,8,9]
print("List l1 ",l1)
print("List l2",l2)
# l1.append(l2)
l1 = l1 + l2
print("List l1 after l2 appended to it :",l1)