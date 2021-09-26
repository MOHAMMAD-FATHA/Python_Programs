"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 14:32 
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 14:32
* @Title: :Python program to create set difference. 
"""

setc1 = set(["green", "blue"])
setc2 = set(["blue", "yellow"])
print("Original sets:")
print(setc1)
print(setc2)
r1 = setc1.difference(setc2)
print("\nDifference of setc1 - setc2:")
print(r1)
r2 = setc2.difference(setc1)
print("\nDifference of setc2 - setc1:")
print(r2)