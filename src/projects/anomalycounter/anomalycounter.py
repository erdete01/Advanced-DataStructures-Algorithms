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
    for x in f: myList.append(list(x.replace("\n","")))
    return (myList)

def count(filename):
  counter = 0
  floodMatrix = rowAndColumn(filename)
  for i in range(len(floodMatrix)):
    for j in range(len(floodMatrix[0])):
      if floodMatrix[i][j] == "*":
        counter += 1
        helper(floodMatrix,i, j)
  return counter
                   
def helper(floodMatrix,i, j):
  # Base case
  if 0<=i<len(floodMatrix) and 0<=j<len(floodMatrix[0]) and floodMatrix[i][j] == "*":
    floodMatrix[i][j] = 7
    helper(floodMatrix, i, j+1) # Right
    helper(floodMatrix, i, j-1) # Left
    helper(floodMatrix, i+1, j) # Up
    helper(floodMatrix, i-1, j) # Down 