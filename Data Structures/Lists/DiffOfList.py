"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 00:07
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 00:09
* @Title: : Python program to get the difference between the two lists.
"""

l1 = [1, 3, 5, 7, 9]
l2=[1, 2, 4, 6, 7, 8]
diff_l1_l2 = list(set(l1) - set(l2))
diff_l2_l1 = list(set(l2) - set(l1))
total_diff = diff_l1_l2 + diff_l2_l1
print(total_diff)