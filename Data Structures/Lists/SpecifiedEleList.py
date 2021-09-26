"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 23:55
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 23:59
* @Title: : Python program to print a specified list after removing the 0th, 4th and
            5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

"""

l1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
l2 = []
for ele in l1:
    if (ele != l1[0] and ele != l1[4] and ele != l1[5]):
        l2.append(ele)
print(l2)