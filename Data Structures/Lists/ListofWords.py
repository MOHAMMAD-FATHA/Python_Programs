"""
* @Author: Mohammad Fatha
* @Date: 2021-09-26 23:50
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-26 23:50
* @Title: : Python program to find the list of words that are longer than n from a
            given list of words.
"""

def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    print(txt)
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "find the list of words that are longer than n from a given list of words"))