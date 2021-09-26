"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to convert a list into a nested dictionary of keys
"""

l = [1,2,3,4]
dict = nes_dict = {}

for ele in l:
    nes_dict[ele] = {}
    nes_dict = nes_dict[ele]
print(dict)
