"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 02:00
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 02:00
* @Title: : Python program to count the number of characters (character frequency) in a string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""

str1 = 'google.com'
dict = {}
for n in str1:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print(dict)

