"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Adding comma separated string to list and tuple
"""
l = [1,'A', 'T', 'H','A']
con_str = ""
for value in l:
    con_str += str(value)
print(con_str)