'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-23 15:10  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-23 15:10
* @Title: Employee Wage Managment System Using OOPS concept and JSON
'''
import random
import json

class EmployeeWage:
    '''
    Description:
        This class is to read the json file which consists details for employee wage
        calculation and store it into dictionary and use its keys and values for monthly wage
        calculation of employee based on its working hours 
            
    '''
    def __init__(self):
        pass
    
    def employee_wage(self,check):
        '''
        Description:
            This function we used switch cases in python, in which we have used dictionary
            as switch case where each key consist of function as value  
        '''
        switcher = {
            0 : self.absent(),
            1 : self.full_day(),
            2 : self.half_day()
            }

        return switcher.get(check)

    def full_day(self):
        '''
        Description:
            This function is used to calculate the full day wage of employee using 
            full day hours and wage per hour from dictionary as its keys and values from json file
        '''
        full_day_wage = self.emp_dict["FULL_DAY_HOURS"] * self.emp_dict["WAGE_PER_HOUR"]
        return full_day_wage

    def half_day(self):
        '''
        Description:
            This function is used to calculate the half day wage of employee using 
            full day hours and wage per hour from dictionary as its keys and values from json file
        '''
        half_day_wage = self.emp_dict["HALF_DAY_HOURS"] * self.emp_dict["WAGE_PER_HOUR"]
        return half_day_wage

    def absent(self):
        '''
        Description:
            This function returns 0 as employee is absent
        '''
        return 0
    
    def read_from_json(self):
        '''
        Description:
            This function read data from json and store it into dictionary and use keys and values 
            of dictionary as per requirements
        '''
        day_wage = 0
        monthly_wage = 0
        day_check = 0
        with open ("F:\.metadata\Python\OOPS Programs\Employee Wage\EmployeeWage.json","r")as emp_file:
            self.emp_dict = json.load(emp_file)
            while day_check < self.emp_dict["MONTHLY_DAYS"] and day_check < self.emp_dict["MONTHLY_HOURS"]:
                wage_check = random.randint(0,2)
                day_wage= employeewage.employee_wage(wage_check)
                print(day_wage)
                monthly_wage += day_wage
                day_check+=1
            print("Employee Monthly Wage is :",monthly_wage) 



if __name__ == '__main__':

    employeewage = EmployeeWage()
    employeewage.read_from_json()

    