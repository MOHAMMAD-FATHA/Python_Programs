"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 02:35
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 02:35
* @Title: : Python program to get the last part of a string before a specified character.
"""
a_string = "docs.python.org"

partitioned_string = a_string.partition('.')
print(partitioned_string)
before_first_period = partitioned_string[0]
print(before_first_period)

str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])