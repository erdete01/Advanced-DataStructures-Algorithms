#!/usr/bin/env python3
"""
A Classy Problem
"""

from typing import Dict, List


def classify(people: dict) -> List[str]:
    """
    Classify people
    
    Return the ordered (highest to lowest) list
    """
    # class_rank = {"upper":5,"middle":4,"lower":3}
    # class_rank = {"upper":5,"middle":4,"lower":3}
    myDict = {}
    for aKey, aValue in people.items():
        myString = ''
        valueList = aValue.split("-")
        valueList = valueList[::-1]
        for i in valueList:
            if i == "upper":
                myString+= "5"
            if i == "middle":
                myString += "4"
            if i == "lower":
                myString += "3"
        myDict[aKey] = myString
    res = list(myDict.values())[0]
    for aKey, aValue in myDict.items():
        if len(aValue) > len(res):
            res = aValue
    almostFinal = {}
    for aKey, aValue in myDict.items():
        if len(aValue) != len(res):
            a = len(res) - len(aValue)
            b = a * '4'
            c = str(aValue) + str(b)
            almostFinal[aKey] = c
        else:
            almostFinal[aKey] = aValue
    rest = list(myDict.values())[0]
    flipped = {}
    for key, value in almostFinal.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
   
    for key, value in flipped.items():
        value.sort()
        flipped[key] = value
       
    dictionary_items = flipped.items()
    sorted_items = sorted(dictionary_items)
    final = []
    for key, value in sorted_items:
        final.append(value)
    final = final[::-1]
    flattened = [val for sublist in final for val in sublist]
    print(flattened)
    return flattened
def read_file(filename: str) -> Dict[str, str]:
    """
    Read data from the file into a dictionary

    Return the {person: class} mapping
    """
    # Time Complexity O(n^2) 
    # because python find method takes linear 
    # and for loop adds one more loop. 
    # Therefore, it's O(n^2)
    f = open(filename, "r")
    myDictionary = dict()
    for x in f: 
        myDictionary[x[0: x.find(':')]] = x[x.find(':') + 1 : x.find('class')]
    return myDictionary
    
def main():
    """Entry point"""
    people = read_file("data/projects/classy/classy01.txt")
    print(classify(people))


if __name__ == "__main__":
    main()
