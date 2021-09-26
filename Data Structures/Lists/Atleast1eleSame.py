"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 23:51
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 23:55
* @Title: : Python program to clone or copy a list.
"""
l1 = [1,2,3,4]
l2 = [4,5,6,7]

for ele1 in l1:
    for ele2 in l2:
        if ele1 == ele2:
            print(True)
            break

            