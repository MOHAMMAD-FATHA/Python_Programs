"""
* @Author: Mohammad Fatha
* @Date: 2021-09-25 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-25 01:52 
* @Title: : Python program to count the values associated with key in a dictionary.
"""
d = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

print("Using Loop ")
temp = 0
for dict1 in d:
    for key in dict1:
        if dict1[key] == True:
            temp +=1
print(temp)
print("Using in built function sum with list comprehension ")
res = sum(x == True for dict2 in d for x in dict2.values() )
print(res)
print(d)