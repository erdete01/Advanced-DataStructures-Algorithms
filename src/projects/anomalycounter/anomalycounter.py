#!/usr/bin/env python3
"""
Anomaly counter
@author: Temuulen Erdenebulgan
"""
# 1. If the current node (cell, pixel) color is equal to the _replacement_ $c'$, return
# 2. If the current node color is **not** equal to _target_, return
# 3. Update color of the current node to $c'$
# 4. Continue the algorithm by expanding the flood to the adjacent nodes (NESW)
# 5. Return

def rowAndColumn(path: str) -> list:
    myList = list()
    f = open(path, "r")
    for x in f: myList.append([x.replace("\n","")])
    return (myList)

def count(filename: str) -> int:
    """Count number of anomalies/blobs in an image"""
    myList = rowAndColumn(filename)
    # Created row and a column
    row, col = len(myList), len(myList[0][0])

def floodFill(myString):
    myStack = []
    counter = 0
    row, col = len(myString), len(myString[0][0])
    for i in range(col):
        for j in range(row):
            if myString[i][j] == "*": 
                myStack.append([i, j])
            else: 
                count
    return counter

    # for i in myList:
    #     # Only Checking the first myList[0], not dynamic.
    #     if i == len(i)*"*":
    #         return 1
    #     for k in i:
    #         if "*" not in k: return 0
    #         else:
    #             pass
    #             # Check East, West, South, and North 
    #             # Maybe convert it into a while loop