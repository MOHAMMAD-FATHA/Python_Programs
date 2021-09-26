"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 19:35
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 19:35
* @Title: :Python program to remove element from tuple
"""
t1 = 2, 4, 5, 6, 2, 3, 4, 4, 7 
print(t1)
#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator you can remove an item and it will create a new tuple
t1 = t1[:2] + t1[3:]
print(t1)
#converting the tuple to list
l1 = list(t1) 
#use different ways to remove an item of the list
l1.remove(3) 
#converting the tuple to list
t1 = tuple(l1)
print(t1)