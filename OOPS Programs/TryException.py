x=input("Enter the number 1: ")
y=input("Enter the number 2: ")

try:
    z= x/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception: ')
    z=None
except Exception as e:
    print("Exception occured type: ",type(e).__name__)
    z=None    
print("Division is ",z)