"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Python script to generate and print a dictionary that contains a number 
            (between 1 and n) in the form (x, x*x).
"""

d = {'Name': ["Fatha","Mohammad","John"], 'Age': [24,35,23], 'Designation': ["Data Engineer","Scientist","Data Scientist"]} 

for row in zip(*([k]+(v) for k,v in d.items())):
    print(*row)
    
# NOT UNDERSTOOD