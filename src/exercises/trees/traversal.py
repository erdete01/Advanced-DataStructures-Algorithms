#!/usr/bin/env python3
"""Turning in-order and post-order tree traversals into pre-order"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_preorder(inorder, postorder):
    # Return pre-order traversal of a tree based on its in-order and post-order traversals
    inorder = list(inorder)
    postorder = list(postorder)
    def rec(inorder, postorder):
        if not inorder or not postorder:
            return
        # This will be always the node
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)
        root.right = rec(inorder[mid+1:], postorder)
        root.left = rec(inorder[:mid], postorder)
        return root
    node =  rec(inorder, postorder)
    return preorder(node)

def preorder(node):
    def convert_String(node, string):
        # Get the treenode and then return preorder
        if node == None or node.val == 0:
            return 
        if node.left == None and node.right == None:
            return str(node.val)
        # Get the first elemenet from the node. It's root
        final_ans = str(node.val)
        # Call it recursively to the left and then add it to the finalAnswer
        if node.left != None:
            final_ans += convert_String(node.left, '')
        else:
            final_ans = final_ans
        # Call it recursively to the right and then add it to the finalAnswer
        if node.right != None:
            final_ans += convert_String(node.right, '')
        return final_ans
    return convert_String(node, '')

def main():
    """This is the main function"""
    print(get_preorder(inorder="UOMELBARTKGSNI", postorder="UMELABORSGNIKT"))


if __name__ == "__main__":
    main()
