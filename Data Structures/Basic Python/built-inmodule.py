"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Program to get built-in modules of the python
"""
import sys

module_name = ', '.join(sorted(sys.builtin_module_names))
print(module_name)