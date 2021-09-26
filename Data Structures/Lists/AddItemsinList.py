"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 23:09
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 23:09 
* @Title: : Python program to sum all the items in a list
"""

l1 = [1,2,3,4,5]
# Using Sum function
l1 = sum(l1)
print("Sum of all the items in list 1:")
print(l1)

l2 = [1,2,3,4,5,6]
sum1 = 0
for ele in l2:
    sum1 += ele
print("Sum of all items in list 2:")
print(sum1)

