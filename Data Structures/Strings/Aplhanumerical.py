"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 02:25
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 02:25
* @Title: : Python program that accepts a comma separated sequence of words as input and 
            prints the unique words in sorted form (alphanumerically).
        Sample Words : red, white, black, red, green, black
        Expected Result : black, green, red, white,red
"""
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))