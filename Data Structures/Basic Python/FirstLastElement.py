"""
* @Author: Mohammad Fatha
* @Date: 2021-09-24 15:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-15 01:52 
* @Title: :Print fist and last element of the give list
"""
# # Print the first and last element of the list
# l = ["Red","Green","White" ,"Black"]
# print("First elemet of list is ",l[0],"Last element of list is ",l[len(l)-1])

# Print document of the given built in function
# print(abs.__doc__)

# # Print the clander of given year and month
# import calendar

# yy = int(input("Enter the year you want:" ))
# mm = int(input("Enter the month you want:" ))
# print(calendar.month(yy,mm))

# calculating the days between given 2 dates
from datetime import datetime
date_format = "%m/%d/%Y"
d0 = input()
d1 = input()
a = datetime.strptime(d0, date_format)
b = datetime.strptime(d1, date_format)
delta = b - a
print(delta.days)