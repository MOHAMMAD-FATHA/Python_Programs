"""
* @Author: Mohammad Fatha
* @Date: 2021-09-27 00:44
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-27 00:44 
* @Title: :Python program to append a list to the second list.
"""
from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)