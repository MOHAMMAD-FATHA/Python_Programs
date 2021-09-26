"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 01:19  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:20
* @Title: :Python program to count number of items in a dictionary value that is a list
"""
dict= {'id':[1, 'success', 'name','Lary'],'id2':[ 2, 'success', 'name','Rabi'],'id3':[ 3, 'success', 'name','Alex']}
count = sum(map(len, dict.values()))
print(count)