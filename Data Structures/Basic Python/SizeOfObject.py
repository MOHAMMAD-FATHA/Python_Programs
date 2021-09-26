"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to get the size of an object in bytes
"""

import sys

str1 = "Fatha"
l= [1,54,23,78,'Abc',661]

print("Size of ",str1,"is",sys.getsizeof(str1),"in bytes")
print("Size of ",l,"is",sys.getsizeof(l),"in bytes")