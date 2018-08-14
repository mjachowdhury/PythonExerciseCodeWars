# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 00:02:57 2018

@author: Mohammed
"""
"""
Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
 
"""

# Function to get no of set bits in binary
# representation of positive integer n */
"""
def countBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>=1
    return count

#function calling     
i = 9
print(countBits(i))
"""


# Python3 implementation of recursive
# approach to find the number of set
# bits in binary representation of 
# positive integer n

"""
def countBits(n):
    #base case
    if (n == 0):
        return 0
    else:
        #if last bit set add 1 else
        # add 0
        return (n & 1) + countBits( n >> 1)

# get value from user
# Function calling
n = 9
print(countBits(n))

"""

# Another way of getting bits ..

def countSetBits(n):
    return bin(n).count("1")

n = 9
print(countSetBits(n))

