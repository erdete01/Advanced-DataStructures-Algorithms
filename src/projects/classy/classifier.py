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
    raise NotImplementedError


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
