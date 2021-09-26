"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to remove a key from a dictionary.
"""
a = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(a)

if 1 in a:
    del a[1]
print(a)