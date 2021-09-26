"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 23:40
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 23:40
* @Title: : Python program to remove duplicates from a list.
"""
l1 = [1,2,1,3,4,1]
l2 = []
for ele in l1:
    if ele not in l2:
        l2.append(ele)
print(l2)