"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :sort three integers without using conditional statements and loops

"""

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
num3 = int(input("Input third number: "))

min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)
mid_num = (num1+num2+num3) - num1 - num3
print("Numbers in sorted order: ", min_num, mid_num, max_num)