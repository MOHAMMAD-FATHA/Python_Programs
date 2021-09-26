"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python script to generate and print a dictionary that contains a number 
            (between 1 and n) in the form (x, x*x).
"""
a = {}
n = 5

for i in range(1,n+1):
    a[i] = i*i
print(a)