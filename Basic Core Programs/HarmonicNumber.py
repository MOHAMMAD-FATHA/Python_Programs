'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-17 00:12  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 00:15
* @Title: To print the Nth Harmonic number of given range
'''
harmonic_range = int(input("Enter the range to calculate Nth Harmonic number "))
harmonic_number = 0

# Start iteration from 1 to given range
for i in range(1,harmonic_range+1):
    if harmonic_range == 0:
        print("Enter the valid range")
    else:
        harmonic_number += 1 / i
print("The Nth Harmonic number is ", harmonic_number)

    