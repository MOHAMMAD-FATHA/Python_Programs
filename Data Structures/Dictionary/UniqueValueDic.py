"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to print all unique values in a dictionary
"""
L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print(type(L))
print("Original List: ",L)
uni_value = set( val for a in L for val in a.values())
print(type(uni_value))
print("Unique Values: ",uni_value)
