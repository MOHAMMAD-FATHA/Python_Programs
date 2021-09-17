"""
* @Author: Mohammad Fatha
* @Date: 2021-09-17 02:05  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 02:15
* @Title: :To find the roots of given quadratic equation
"""
import math as m

def quadratic_equation():

    """
    Description:
        In this function we find the roots of quadratic equation
        a, b, c are the three inputs to find the delta value.
        The value of delta should be greater than 0 to have real roots.
    """    

    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    # Getting the value of delta.
    delta = (b * b - 4 * a * c)

    # Finding the roots if value of delta is greater than 0.
    if(delta > 0):
        root1 = (-b + m.sqrt(delta)) / (2 * a)
        root2 = (-b - m.sqrt(delta)) / (2 * a)

        print("First root of equation is: ",root1)
        print("Second root of equation is: ",root2)
    else:
        print("There are no real two roots for the given values")

if __name__ == '__main__':
    quadratic_equation()   