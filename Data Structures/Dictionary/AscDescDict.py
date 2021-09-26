"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to script to sort (ascending and descending) a dictionary by value. 
"""

import operator

a = {0:2,1:4,2:3}
print('Original dictionary : ',a)
sorted_d = dict(sorted(a.items(), key= operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(a.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
