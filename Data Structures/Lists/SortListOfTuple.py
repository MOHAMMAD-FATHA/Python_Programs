"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 23:20
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 23:20
* @Title: : Write a Python program to get a list, sorted in increasing order by the last
            element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

def sort(tuples):
    return sorted(tuples, key=last)

def last(n):
    return n[-1] 

a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("Sorted:")
print(sort(a))