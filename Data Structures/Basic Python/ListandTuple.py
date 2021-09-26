"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Adding comma separated string to list and tuple
"""
num = input("Enter numbers to add into list and tuple:")
l = []
l = num.split(",")
print(l)
t = tuple(l)
print(t)