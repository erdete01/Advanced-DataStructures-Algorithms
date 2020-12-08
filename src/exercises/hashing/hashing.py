#!/usr/bin/env python3
"""Hashing functions"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    a = key%size
    return a


def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    squared = key * key
    str_squared = str(squared)
    mid = len(str_squared) // 2
    return int(str_squared[mid-1:mid+1]) % size


def hash_folding(key: int, size: int) -> int:
    """Find hash using folding method"""
    stringSplit = key.split('-')
    myNumbers = ''
    for i in stringSplit:
        myNumbers += i
    myList = []
    for i in range(1, len(myNumbers), 2):
        total = str(myNumbers[i-1]) + str(myNumbers[i])
        myList.append(total)
    totalNum = 0
    for i in myList:
        totalNum += int(i)
    return (totalNum % size)


def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    myNum = 0
    for i in range(len(key)):
        myNum += ord(key[i])
    return (myNum % size)


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    myNum = 0
    for i in range(len(key)):
        myNum += ord(key[i])*i
    return (myNum % size)

