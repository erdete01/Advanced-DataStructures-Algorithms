#!/usr/bin/env python3
"""Hashing functions"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    return key%size


def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    mid = len(str(key * key)) // 2
    return int(str(key * key)[mid-1:mid+1]) % size


def hash_folding(key: int, size: int) -> int:
    """Find hash using folding method"""
    myNumbers = ''
    for i in key.split('-'):
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

