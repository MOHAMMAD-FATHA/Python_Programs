"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 19:00
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 19:05 
* @Title: :Python program to unpack a tuple in several variables
"""

#create a tuple
tuple1 = (4, 8, 3)
print(tuple1,type(tuple1))
n1, n2, n3 = tuple1
#unpack a tuple in variables
print(n1 + n2 + n3) 
#the number of variables must be equal to the number of items of the tuple
n1, n2, n3, n4= tuple1 
