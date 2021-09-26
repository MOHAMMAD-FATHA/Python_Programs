"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 19:05
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 19:10 
* @Title: :Python program to create the clone of a tuple
"""
from copy import deepcopy

#create a tuple
tuplex = ("HELLO", 5, [], True) 
print(tuplex)
#make a copy of a tuple using deepcopy() function
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)