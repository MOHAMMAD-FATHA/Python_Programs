"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Create a histogram from a given list of integers
"""
items = [6, 1, 20, 9,1]
for n in items:
    output = ''
    times = n
    while( times > 0 ):
        output += '$'
        times = times - 1
    print(output)
