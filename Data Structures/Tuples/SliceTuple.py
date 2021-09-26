"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 19:40
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 19:40 
* @Title: :Python program to slice the tuple
"""
#create a tuple
t1 = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
s1 = t1[3:5]
#is exclusive
print(s1)
#if the start index isn't defined, is taken from the beg inning of the tuple
s1 = t1[:6]
print(s1)
#if the end index isn't defined, is taken until the end of the tuple
s1 = t1[5:]
print(s1)
#if neither is defined, returns the full tuple
s1 = t1[:]
print(s1)
#The indexes can be defined with negative values
s1 = t1[-8:-4]
print(s1)
#create another tuple
t1 = tuple("HELLO WORLD")
print(t1)
#step specify an increment between the elements to cut of the tuple
#tuple[start:stop:step]
s1 = t1[2:9:2]
print(s1)
#returns a tuple with a jump every 3 items
s1 = t1[::4]
print(s1)
#when step is negative the jump is made back
s1 = t1[9:2:-4]
print(s1)