#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """

    # Parse data from the 'data/vocab.txt' file.
    # - The file is saved in tab-separated values (TSV) format.
    # - Each line contains a word's ID and the word itself.
    # The output dictionary should map word's ID on the word itself, e.g.:
    #   {1: 'aa', 2: 'ab', ...}

    filepath = os.path.join(os.path.dirname(__file__), "data", 'vocab.txt')
    with open(filepath, 'r') as v:
        data = v.readlines()

    vocabulary_dict = dict()

    for line in data:
        key, value = line.strip().split('\t')
        vocabulary_dict[int(key)] = value

    return vocabulary_dict
