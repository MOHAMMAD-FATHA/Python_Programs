"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 23:30
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 23:30
* @Title: : Python program to count the number of strings where the string length
            is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

l1 = ['pop', 'xyz', 'FATHA', '1221']
ctr = 0

for word in l1:
    if len(word) > 1 and word[0] == word[-1]:
        ctr += 1
print(ctr)

