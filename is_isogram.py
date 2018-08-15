# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 00:39:06 2018

@author: Mohammed
"""

#Problem Statement
"""
An isogram is a word that has no repeating letters, consecutive or 
non-consecutive. Implement a function that determines whether a string 
that contains only letters is an isogram. Assume the empty string is an 
isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""

#both program is working 

def is_isogram(string):
    if type(string) != str:
        raise TypeError('Argument should be a string')
    elif string == " ":
        return (string, False)
    else:
        
        string = string.lower()
        for i in string:
            if string.count(i) > 1:
                return False
    return True

print(is_isogram("abcdabcdABCD"))

#both program is working 

def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True


"""
def is_isogram(string):
    return len(string) == len(set(string.lower()))

"""