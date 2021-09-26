"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 00:21
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 00:22 
* @Title: :Python program to append a list to the second list.
"""
import collections

l1 = [2, 1, 4, 3, 5]
l2 = [1, 2, 4, 3, 5]
  
# printing lists
print ("The first list is : " + str(l1))
print ("The second list is : " + str(l2))

# sorting both the lists
l1.sort()
l2.sort()
  
# using == to check if 
# lists are equal
if l1 == l2:
    print ("The lists are identical")
else :
    print ("The lists are not identical")


l3 = [6, 1, 4, 3, 5]
l4 = [1, 2, 4, 3, 5]
# printing lists
print ("The first list is : " + str(l3))
print ("The second list is : " + str(l4))

# using collections.Counter() to check if 
# lists are equal
if collections.Counter(l3) == collections.Counter(l4):
    print ("The lists are identical")
else :
    print ("The lists are not identical")