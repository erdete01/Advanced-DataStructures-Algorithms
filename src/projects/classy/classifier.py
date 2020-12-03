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
    # ["Beaver", "Elephant", "Aardvark", "Cheetah", "Dolphin"],
    # Why Dolphine is After Cheetah. Not sure. 
    # My Brute Force Solution might be iterate through the dictionary
    # And at the same time, I will also iterate through myList 3 times. It will be 
    # Time Complexity O(n^2)
    # people = {"Ant": "upper", "Bee": "middle", "Cat": "lower"}
    myList = {}
    finalList = []
    for aKey, aValue in people.items():
        if len(myList) > 0:
            for x, y in myList.items():
                if y == "upper":
                    myList[x] y
                elif y =="middle":
                    if y == "upper":
                        myList.insert(i-1,  aValue)
                        i += 1
                    else:
                        myList.append(aValue)
                        i += 1
                else:
                    myList.insert(i-1, aValue)
                    i += 1
        else:
            myList[aKey] = aValue
    print(myList)
    


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
