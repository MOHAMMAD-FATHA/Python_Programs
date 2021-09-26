"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 02:10
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 02:10
* @Title: : Python program to get a string from a given string where all occurrences of its
            first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""

str1 = "restart"
char = str1[0]
str1 = str1.replace(char, '$')
str1 = char + str1[1:]

print(str1)
