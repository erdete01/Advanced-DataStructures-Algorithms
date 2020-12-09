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
    """Find hash using folding method"""
    if '-' in key:
        myNumbers = ''
        for i in key.split('-'):
            myNumbers += i
        if int(len(myNumbers)) % 2 != 0:
            converting = []
            for i in range(1, len(myNumbers), 2):
                converting.append((str(myNumbers[i-1]) + str(myNumbers[i])))
            converting.append(myNumbers[-1])
        else:
            converting = []
            for i in range(1, len(myNumbers), 2):
                converting.append((str(myNumbers[i-1]) + str(myNumbers[i])))
        totalNum = 0
        for i in converting:
            totalNum += int(i)
        return (totalNum % size)
    if '/' in key:
        myNumbers = ''
        for i in key.split('/'):
            myNumbers += i
        if int(len(myNumbers)) % 2 != 0:
            converting = []
            for i in range(1, len(myNumbers), 2):
                converting.append((str(myNumbers[i-1]) + str(myNumbers[i])))
            converting.append(myNumbers[-1])
        else:
            converting = []
            for i in range(1, len(myNumbers), 2):
                converting.append((str(myNumbers[i-1]) + str(myNumbers[i])))
        totalNum = 0
        for i in converting:
            totalNum += int(i)
        return (totalNum % size)
    if '.' in key:
        myNumbers = ''
        for i in key.split('.'):
            myNumbers += i
        if int(len(myNumbers)) % 2 != 0:
            converting = []
            for i in range(1, len(myNumbers), 2):
                converting.append((str(myNumbers[i-1]) + str(myNumbers[i])))
            converting.append(myNumbers[-1])
        else:
            converting = []
            for i in range(1, len(myNumbers), 2):
                converting.append((str(myNumbers[i-1]) + str(myNumbers[i])))
        totalNum = 0
        for i in converting:
            totalNum += int(i)
        return (totalNum % size)
    if '(' in key or ')' in key:
        i = 0
        myList = []
        while i < len(key):
            if len(myList) == 0:
                myList.append(key[i])
                i += 1
            else:
                if myList[-1] == '(':
                    myList.pop()
                    
                elif myList[-1] == ')':
                    myList.pop()
                    
                elif myList[-1] == ' ':
                   myList.pop()
                else:
                    myList.append(key[i])
                    i += 1
        myNumbers = "" 
        myNumbers = (myNumbers.join(myList)) 
        if int(len(myNumbers)) % 2 != 0:
            converting = []
            for i in range(1, len(myNumbers), 2):
                converting.append((str(myNumbers[i-1]) + str(myNumbers[i])))
            converting.append(myNumbers[-1])
        else:
            converting = []
            for i in range(1, len(myNumbers), 2):
                converting.append((str(myNumbers[i-1]) + str(myNumbers[i])))
        totalNum = 0
        for i in converting:
            totalNum += int(i)
        return (totalNum % size)

    if key.isdigit():
        if int(len(key)) % 2 != 0:
            converting = []
            for i in range(1, len(key), 2):
                converting.append((str(key[i-1]) + str(key[i])))
            converting.append(key[-1])
        else:
            converting = []
            for i in range(1, len(key), 2):
                converting.append((str(key[i-1]) + str(key[i])))
        totalNum = 0
        for i in converting:
            totalNum += int(i)
        return (totalNum % size)
    else:
        myNumbers = [i.strip() for i in key.split(',')]
        myList = []
        for i in myNumbers:
            if " " in i:
                a = i.split(' ')
                for x in a:
                    myList.append(x)
            else:
                myList.append(i)
        myNum = ''
        for i in myList:
            if i.isdigit():
                myNum += str(i)
        
        if int(len(myNum)) % 2 != 0:
            converting = []
            for i in range(1, len(myNum), 2):
                converting.append((str(myNum[i-1]) + str(myNum[i])))
            converting.append(myNum[-1])
        else:
            converting = []
            for i in range(1, len(myNum), 2):
                converting.append((str(myNum[i-1]) + str(myNum[i])))
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

