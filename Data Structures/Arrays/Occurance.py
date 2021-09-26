"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to check occurence of specific element in array
"""

import array as arr

array_num = arr.array('i',[1,1,1,2,3,4,5,6])

n= int(input("Enter number to check occurence in array : "))
count = array_num.count(n)
print(f"Occurence of {n} in array are {count}")