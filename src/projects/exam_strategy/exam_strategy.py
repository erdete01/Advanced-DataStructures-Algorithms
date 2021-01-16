from collections import namedtuple
from typing import List, Tuple

Item = namedtuple("Item", ["value", "weight"])


def knapsack(capacity: int, items: List[Item]) -> List[int]:
    """
    General Knapsack solution.

    This function takes the knapsack capacity and the list of items (named tuples) to consider.
    The function returns a list of chosen indices.
    This function is optional but highly recommended.
    Use of the named tuple Item is optional but encouraged.
    """ 
    # Get all the weights and values
    value, weight, myMatrix = [], [], []
    for i in items: value.append(i[0])
    for i in items: weight.append(i[1])
    row = weight[0]
    # First law. Create all 0
    myMatrix = [[0 for i in range(capacity+1)] for i in range(row+1)]
    # Add second and third law
    value.pop(0)
    weight.pop(0)
    for i in range(row + 1): 
        for j in range(capacity + 1): 
            if i == 0 or j == 0:  myMatrix[i][j] = 0
            # Third law
            elif weight[i-1] <= j: myMatrix[i][j] = max(value[i-1] + myMatrix[i-1][j-weight[i-1]],  myMatrix[i-1][j]) 
            # Second law
            else: myMatrix[i][j] = myMatrix[i-1][j] 
    
    # Now I have the Matrix build. I have to select the ones that maximizes the exam strategy
    #Let's get the last item of the matrix  
    c, w, res = myMatrix[row][capacity], capacity, list()
    for i in range(row, 0, -1): 
        if myMatrix[row][capacity] <= 0: break 
        elif myMatrix[row][capacity] == myMatrix[i - 1][w]: continue
        else: 
            res.append([i-1])
            res.append(weight[i - 1]) 
            myMatrix[row][capacity] -= value[i - 1] 
            w -= weight[i - 1] 
    final=[j for i in res[::2] for j in i]
    final.reverse()
    return [final, c]


def pick_questions_to_answer(filename: str) -> Tuple[List[int], int]:
    """
    Main selection function

    This function takes file name as an argument.
    The function returns a tuple of two items: the list of chosen indices and total point value of all selected questions.
    """
    myList = []
    with open(filename) as f:
        for aline in f:
            aline = aline.split()
            if aline:          
                aline = [int(float(i)) for i in aline]
                myList.append(aline)
    return (knapsack(myList[0][0], myList))


def main():
    """Entry point"""
    for i in range(1, 6):
        filename = f"data/projects/exam_strategy/questions{i}.in"
        selection = pick_questions_to_answer(filename)
        print(
            f"Case {i}: Items {sorted(selection[0])} sum up to {selection[1]}"
        )


if __name__ == "__main__":
    main()