#!/usr/bin/env python3
"""Hashing functions"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    return key%size


def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    return int(str(key * key) \
        [len(str(key * key)) // 2-1:len(str(key * key)) // 2+1]) % size


def hash_folding(key: int, size: int) -> int:
    """Find hash using folding method"""
    myNumbers = ''
    for i in key.split('-'):
        myNumbers += i
    converting = [str(myNumbers[i-1]) + str(myNumbers[i]) \
         for i in range(1, len(myNumbers), 2)]
    totalNum = 0
    for i in converting:
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

