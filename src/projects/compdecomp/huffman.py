#!/usr/bin/env python3
"""Huffman coding"""


import argparse
import heapq
import json
import logging
import pathlib
from collections import Counter, OrderedDict
from typing import List, Tuple, Union

DATA_DIR = pathlib.Path("data/projects/compdecomp/")


class Node:
    """Class Node"""

    def __init__(self, value, weight: int, left=None, right=None):
        """
        value: letter in the text
        weight: number of times the letter appears in the text
        left: left child in the Huffman tree
        right: right child in the Huffman tree
        """
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f"Node({self.value}, {self.weight}, {self.left}, {self.right})"


def build_tree(all_freq: dict) -> Node:
    """
    Construct a Huffman tree from the text

    :param all_freq: frequency table
    :return tuple the tree root
    """
    heap: List[Node] = []
    # TODO: Implement this function
    for keys, values in all_freq.items():
        myNode = Node(keys, values)
        heapq.heappush(heap, myNode)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(heap, node1.weight + node2.weight)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    return(merged)    



def traverse_tree(root: Node) -> str:
    """
    Traverse a tree pre-order and return the result

    :param root: tree root
    :return values of a tree
    """
    left = []  
    right = []  
    left.append(root)  
    while len(left) > 0:  
        node = left.pop()  
        # If Leaf, add the values
        if node.left is None and node.right is None:  
            right.append(node)  
        else:
            if node.left is not None: 
                left.append(node.left)  
            if node.right is not None:  
                left.append(node.right)  
    # Right has all the root values
    res = ''
    for i in range(0, len(right)):
        res += right.pop().value
    return ' '.join(res) 

def follow_tree(tree: Node, code: str) -> Union[str, None]:
    """
    Follow the code through the tree

    :param tree: tree root
    :param code: code to find
    :return node value or None
    """
    # Give left 0 and right 1
    ans = None
    for i in code:
        if i == '0':
            tree = tree.left
        if i == '1':
            tree = tree.right
        if tree.left == None and tree.right == None:
            ans = tree.value
    return ans


def mark_tree(d1: dict, d2: dict, root: Node, path: str) -> Union[None, tuple]:
    """
    Generate code for each letter in the text

    :param d1: character-to-code mapping
    :param d2: code-to-character mapping
    :param root: tree root
    :param path: path to the current node
    :return (d1, d2) tuple
    """
    if root.left is None and root.right is None:
        d1[root.value] = path
        d2[path] = root.value
        return

    if root.left is not None:
        if root.left not in d1.keys():
            mark_tree(d1, d2, root.left, path + '0')

    if root.right is not None:
        if root.right not in d1.keys():
            mark_tree(d1, d2, root.right, path + '1')

    return (d1, d2)

def print_codes(d: dict, weights: dict) -> None:
    """
    Print letters of the text and their codes. The output is ordered by the letter weight.

    :param d: character-to-code mapping
    :param weights: character-to-frequency mapping
    """
    print(f"{'Letter':10s}{'Weight':^10s}{'Code':^10s}{'Length':^5s}")
    # TODO: Implement this function
    raise NotImplementedError


def load_codes(codes: dict) -> Node:
    """
    Build the Huffman tree from the stored code-to-character mapping

    :param codes: code-to-character mapping
    :return root of the Huffman tree
    """
    # Building Node
    root = Node(None, None)
    cur = root
    for i in codes:
        val = codes[i]
        for j in range(len(i)):
            if j == len(i) - 1:    
                if i[j] == '0' and cur.left == None:
                    node = Node(None, None)
                    node.value = val
                    cur.left = node
                if i[j] == '1' and cur.right == None:
                    node = Node(None, None)
                    node.value = val
                    cur.right = node
                if i[j] == '0' and cur.left != None:
                    node = cur.left
                    node.value = val
                if i[j] == '1' and cur.right != None:
                    node = cur.right
                    node.value = val
            else:
                if i[j] == '0' and cur.left == None:
                    node = Node(None, None)
                    cur.left = node
                    cur = cur.left
                if i[j] == '1' and cur.right == None:
                    node = Node(None, None)
                    cur.right = node
                    cur = cur.right
                if i[j] == '0' and cur.left != None:
                    cur = cur.left
                if i[j] == '1' and cur.right != None:
                    cur = cur.right
        cur = root
    return root

def compress(text: str, codes: dict) -> Tuple[bytes, int]:
    """
    Compress text using Huffman coding

    :param text: text to compress
    :param codes: character-to-code mapping
    :return (packed text, padding length) tuple
    """
    # TODO: Implement this function
    myList = list()
    padding = str()
    myList = [codes[letter]for letter in text]
    myList = "".join(myList)
    while len(myList) % 8 > 0:
        padding += "0"
        myList += "0"
    myBytes = bytearray()
    i = 0
    while i < len(myList):
        byte = myList[i:i+8]
        myBytes.append(int(byte, 2))
        i += 8
    return (bytes(myBytes), len(padding))


def decompress(bytestream: bytes, padding: int, tree: Node) -> str:
    """
    Decompress binary data using Huffman coding

    :param bytestream: bytes from the archived file
    :param padding: padding length
    :param tree: root of the Huffman tree
    :return decompressed (decoded) text
    """
    # TODO: Implement this function
    binaryNumbers = bin(int.from_bytes(bytestream, byteorder = "big"))[2:]
    binaryNumbers = "0" + str(binaryNumbers)
    removePadding = binaryNumbers[:-padding]
    print(binaryNumbers)
    ## Not sure how to decompress



def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Greet the audience")
    parser.add_argument(
        "-d",
        "--debug",
        help="Enable debug mode",
        action="store_const",
        dest="loglevel",
        const=logging.DEBUG,
        default=logging.WARNING,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Enable verbose mode",
        action="store_const",
        dest="loglevel",
        const=logging.INFO,
    )
    args = parser.parse_args()
    logging.basicConfig(format="%(levelname)s: %(message)s", level=args.loglevel)
    logging.info("Starting up")

    input_files = ["dead_dad", "alphabet", "example", "preamble"]

    for filename in input_files:
        logging.info("Building the tree")
        with open(DATA_DIR / pathlib.Path(f"{filename}.txt"), "r") as text_file:
            text = text_file.read().strip()
        weights = Counter(text)
        root = build_tree(weights)
        char_to_code, code_to_char = mark_tree({}, {}, root, "")

        logging.info("Text statistics")
        print(f"\n{text}")
        print_codes(char_to_code, weights)
        logging.debug(char_to_code)
        logging.debug(code_to_char)
        logging.debug(traverse_tree(root))

        logging.info("Compressing the text")
        archive, padding_length = compress(text, char_to_code)
        code_to_char["padding"] = padding_length
        print(
            f"Text: {text[:5]} ... {text[-5:]}. Compression ratio: {len(archive) / len(text):.3f}"
        )
        logging.debug(archive)

        logging.info("Loading codes from the file")
        with open(DATA_DIR / pathlib.Path(f"{filename}.json"), "r") as code_file:
            metadata = json.load(code_file)
        root = load_codes(metadata)
        padding_length = metadata.get("padding", 0)
        logging.debug(traverse_tree(root))

        logging.info("Decompressing the archive")
        with open(DATA_DIR / pathlib.Path(f"{filename}.bin"), "rb") as data_file:
            result = decompress(data_file.read(), padding_length, root)
        print(result)


if __name__ == "__main__":
    main()
