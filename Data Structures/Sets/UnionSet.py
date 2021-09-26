"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 14:30  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 14:30
* @Title: :Python program to iteration over sets 
"""

setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
print("Original sets:")
print(setc1)
print(setc2)
setc = setc1.union(setc2)
print("\nUnion of above sets:")
print(setc)
setn1 = set([1, 1, 2, 3, 4, 5])
setn2 = set([1, 5, 6, 7, 8, 9])
print("\nOriginal sets:")
print(setn1)
print(setn2)
print("\nUnion of above sets:")
setn = setn1.union(setn2)
print(setn)