#!/usr/bin/env python3
"""
Testing the compress/decompress project
@author: Roman Yasinovskyy
@date: 2020
"""

import json
import pathlib
from collections import Counter

import pytest
import toml
from src.projects.compdecomp import (
    build_tree,
    traverse_tree,
    follow_tree,
    mark_tree,
    compress,
    decompress,
    load_codes,
)

DATA_DIR = pathlib.Path("data/projects/compdecomp/")
TIME_LIMIT = 1


def get_cases(category: str, attribs: tuple):
    with open(pathlib.Path(__file__).with_suffix(".toml")) as f:
        all_cases = toml.load(f)
        for case in all_cases[category]:
            yield [case.get(a) for a in attribs]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, total_weight",
    get_cases("test_case", ("text", "total_weight")),
)

def test_build_tree(text, total_weight):
    #Test the tree building
    weights = Counter(text)
    root = build_tree(weights)
    assert root.weight == total_weight


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, tree",
    get_cases("test_case", ("text", "tree")),
)
def test_traverse_tree(text, tree):
    #Testing the tree traversal
    weights = Counter(text)
    root = build_tree(weights)
    assert traverse_tree(root) == tree


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, code2char",
    get_cases("test_case", ("text", "code2char")),
)


def test_follow_tree_to_leaf(text, code2char):
    #Testing the tree following with a valid result
    weights = Counter(text)
    root = build_tree(weights)
    codes = json.loads(code2char)
    for code in codes:
        assert follow_tree(root, code) == codes[code]


@pytest.mark.timeout(TIME_LIMIT)
@pytest.mark.parametrize(
    "text, code2char",
    get_cases("test_case", ("text", "code2char")),
)
def test_follow_tree_to_none(text, code2char):
    #Testing the tree following with no result
    weights = Counter(text)
    root = build_tree(weights)
    codes = json.loads(code2char)
    if "0" not in codes:
        assert follow_tree(root, "0") is None
    if "1" not in codes:
        assert follow_tree(root, "1") is None

if __name__ == "__main__":
    pytest.main(["-v", "test_compdecomp.py"])
