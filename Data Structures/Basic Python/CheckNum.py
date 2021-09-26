"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Check wheatherthe number is present in group or not
"""

def is_group_member(group_data, n):
    for value in group_data:
       if n == value:
           return True
    return False

n = int(input("Enter the number you want to search :"))
print(is_group_member([1, 5, 8, 3], n))
print(is_group_member([5, 8, 3], n))