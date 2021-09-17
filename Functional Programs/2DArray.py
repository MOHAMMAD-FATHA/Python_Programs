"""
* @Author: Mohammad Fatha
* @Date: 2021-09-17 01:50  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 01:52 
* @Title: :To print 2D array.
"""
def array2D():

    """
    Description:
        This function is to take elements form user input as numer of rows 
        and columns and then print the 2D array.
        Using nested for loop all the elements are printed.
    """  
    rows = int(input("Enter the number of rows"))
    col = int(input("Enter the number of columns"))

    mat2d = []

     # To create a 2D array.
    for i in range(rows):
        arr = []
        for j in range(col):
            arr.append(int(input("Enter the element in 2D array")))
        mat2d.append(arr)
    # To print the elements.
    print("The 2D array for entered elemets is: ")
    for i in range(rows):
        for j in range(col):
            print(mat2d[i][j], end=" ")
        print()


if __name__ == '__main__':
    array2D()
    