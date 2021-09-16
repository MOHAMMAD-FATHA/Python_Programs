'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-17 00:54  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 00:58
* @Title: User Input and Replace String Template “Hello <<UserName>>, How are you?
'''
import re

str = "Hello <<UserName>>, How are you?"
name = input("Enter the user name : ")

if re.match("[A-Z]{1}[a-z]{2,}$", name):
    new_str = str.replace("<<UserName>>", name)
    print(new_str)
else:
    print("Enter a valid name")