"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to print arrays in reverse
"""

import array as arr

array_num = arr.array('i',[1,2,3,4,5,6])

print("Original array")
print(array_num)
# Reverse the array using silice method
print("Reverse array using slice method ")
array_num1 = array_num[::-1]
print(type(array_num1))
print(array_num1)

# new array using reverse function
print("Reverse using reverse function")
array_num.reverse()
print(array_num)