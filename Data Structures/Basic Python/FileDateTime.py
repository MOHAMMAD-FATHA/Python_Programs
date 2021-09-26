"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Program to calculate the time for executing a method
"""
import os.path, time

print("Last modified: %s" % time.ctime(os.path.getmtime("FileDateTime.py")))
print("Created: %s" % time.ctime(os.path.getctime("FileDateTime.py")))
