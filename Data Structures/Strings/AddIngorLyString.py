"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 02:15
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 02:15
* @Title: : Python program to get string in list of strings
"""
def add_string(str1):
    length = len(str1)

    if length > 2:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'

    return str1
print(add_string('abc'))
print(add_string('string'))