"""
* @Author: Mohammad Fatha
* @Date: 2021-09-17 14:17  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 14:20
* @Title: :Sum of three integer adds to Zero
"""
# iterate through list to add element into it
def sum_all_zero(n,l):

    """
    Description:
        This function is to take elements form driver function i,e list
        and length of list.
        Using nested for loops we are adding three pairs of elements with eachother and 
        calculating that its Sum is zero or not
    """
    found = False
    print("All elements in list whose sum is zero are")

    # Iterate through each element and add with other elements to check its sum is zero
    for i in range(0, l-2):

        for j in range(i+1, l-1):

            for k in range(j+1, l):

                if (n[i] + n[j] + n[k] == 0):
                    print(n[i],n[j], n[k])
                    found = True

    # if we don't found any element whose sum is zero
    if(found == False):
        print("Elements whose Sum is zero are not present in list")


if __name__ == '__main__':
    number_of_element = int(input("Enter the number of elements you want to add in list : "))
    num_list = []
    
    for i in range(0,number_of_element):
        element = int(input())
        num_list.append(element)
    len_list = len(num_list)


sum_all_zero(num_list,len_list)