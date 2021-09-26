"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python program to concatenate the 3 dictionary to one dictionary
"""

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4 = {}

for d in (dic1,dic2,dic3) : dic4.update(d)
print(dic4)