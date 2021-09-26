"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to create an array of 5 integers and display the array items. 
            Access individual element through indexes
"""

import array as arr

array_num = arr.array('i',[1,2,3,4,5,6])

for i in array_num:
    print(i)

print("Print first three items individually")
print(array_num[0],array_num[1],array_num[2])