#!/usr/bin/env python3
"""
Anomaly counter
@author: Temuulen Erdenebulgan
"""


def count(filename: str) -> int:
    """Count number of anomalies/blobs in an image"""
    myList = []
    f = open(filename, "r")
    for x in f: myList.append(x.replace("\n",""))
    print(myList)
    for i in myList:
        # Only Checking the first myList[0], not dynamic.
        if i == len(i)*"*":
            return 1
        for k in i:
            if "*" not in k: return 0
            else:
                pass
                # Check East, West, South, and North 
                # Maybe convert it into a while loop