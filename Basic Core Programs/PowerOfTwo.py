'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-17 00:12  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 00:15
* @Title: To print the power of two till the entered range and should be 0 <= N < 31
'''

power_of_two = int(input("Enter the number to get power of two "))

print("i   2 ^ i")
if (0<= power_of_two < 31):
    for i in range(power_of_two): # Iterating till the entered range.
        print(i,"   ",pow(2,i))
else:
    print("Enter the proper range")
