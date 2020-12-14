#!/usr/bin/env python3
"""Turning in-order and post-order tree traversals into pre-order"""


def get_preorder(inorder: str, postorder: str) -> str:
    """Return pre-order traversal of a tree based on its in-order and post-order traversals"""
    # This will be always the node
    theNode = postorder[-1]
    # Find theNode in inorder string
    sub = inorder.find(theNode)
    leftTree = inorder[0: sub]
    rightTree = inorder[sub+1::]
    # Feel like I shoud use recursion
    return theNode+ leftTree+rightTree


def main():
    """This is the main function"""
    print(get_preorder(inorder="UOMELBARTKGSNI", postorder="UMELABORSGNIKT"))


if __name__ == "__main__":
    main()
