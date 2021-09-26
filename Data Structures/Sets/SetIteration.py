"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 14:16  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 14:16
* @Title: :Python program to iteration over sets 
"""

#Create a set 
num_set = set([0, 1, 2, 3, 4, 5])
for n in num_set:
  print(n, end=' ')
print("\n\nCreating a set using string:")
char_set = set("w3resource")  
# Iterating using for loop
for val in char_set:
    print(val, end=' ')