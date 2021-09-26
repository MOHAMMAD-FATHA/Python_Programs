"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to sort files by date

"""
import os
os.chdir('F:')
result = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)
print('\n'.join(map(str, result)))