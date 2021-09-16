'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-17 00:40  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 00:42
* @Title: To print the prime factors of the given number
'''
Num = int(input("Enter the number to find it's prime factors : "))

print("Prime factors of the given number {0} are".format(Num))

for i in range(1,Num+1):
    temp = Num % i
    if temp == 0:
        print(i)
