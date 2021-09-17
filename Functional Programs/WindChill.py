import math as m

"""
* @Author: Mohammad Fatha
* @Date: 2021-09-17 14:30  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 14:35
* @Title: :Calculating wind chill using given Temperature and Wind speed
"""

def wind_chill():

    """
    Description:
        This function is used to find the wind chill.
        Temperature and wind speed are inputs from user.
        To find the wind chill temperature should not be greater than 50,
        and wind speed should be in between 3-120.
    """    

    temperature = float(input("Enter temperature in fahrenheit in between the range 0 to 50: "))
    windSpeed = float(input( "Enter wind speed in between the range 3 to 120: "))

    if(temperature > 50 or windSpeed < 3 or windSpeed > 120):
        print("Wind chill cannot be found for the entered condition")

    else:
        windChill = 35.74 + 0.6215 * temperature +(0.4275*temperature + 35.75)*m.pow(windSpeed,0.16)
        print("Wind chil for the given temperature and wind speed is: ",windChill)

if __name__ == "__main__":
    wind_chill() 