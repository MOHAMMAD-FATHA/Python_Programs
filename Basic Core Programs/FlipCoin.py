'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-16 23:48  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-16 23:50
* @Title: Flip Coin and print percentage of Heads and Tails
'''

import random

toss_num = int(input("Enter the number of flips : "))
tail = 0
head = 0

for i in range(toss_num):
    toss = random.random()
    if toss < 0.5:
        print("Tail")
        tail += 1
    else:
        print("Head")
        head += 1

# Calculating the percentage of tails and heads.

tail_percentage = (tail*100)/toss_num;
head_percentage = 100 - tail_percentage

print("Percentage of head is ",head_percentage,"percentage of tail is ",tail_percentage)

