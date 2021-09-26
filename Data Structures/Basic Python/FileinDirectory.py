"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: : Program to check list all files present in directory

"""

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('F:\.metadata\Python\Data Structures\Basic Python') if isfile(join('F:\.metadata\Python\Data Structures\Basic Python', f))]
print(files_list);
