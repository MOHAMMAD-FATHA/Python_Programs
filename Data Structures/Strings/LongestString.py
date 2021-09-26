"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 02:10
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 02:10
* @Title: : Python program to get string in list of strings
"""
# initialize list 
test_list = ['gfg', 'is', 'best', 'for', 'geeks']
  
# printing original list 
print("The original list : " + str(test_list))
  
# Longest String in list
# using loop
max_len = -1
for ele in test_list:
    if len(ele) > max_len:
        max_len = len(ele)
        res = ele
  
# printing result
print("Maximum length string is : " + res)