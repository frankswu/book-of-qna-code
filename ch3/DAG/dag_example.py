#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: ch3/DAG/dag_example.py
# Author: Hai Liang Wang
# Date: 2018-05-30:18:22:33
#
#===============================================================================

import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    raise "Must be using Python 3"
else:
    unicode = str

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-11:22:32:26"


default_dictionary = dict({
    "刘": [10, 'nz'],
    "刘德": [10, 'nz'],
    "刘德华": [10, 'nz']
})

def get_DAG(sentence, dictionary=default_dictionary):
    DAG, N = {}, len(sentence)
    for k in range(N):
        suffix, i = [], k
        word = sentence[k]
        while i < N and word in dictionary:
            if dictionary[word][0] > 0:
                suffix.append(i)
            i += 1
            word = sentence[k:i + 1]
        if len(suffix) == 0:
            suffix.append(k)
        DAG[k] = suffix
    return DAG

def main():
    sentence = "刘德华演唱了忘情水"
    lis = [x for x in sentence]
    fs = '{:>2} {:>12}' + ' {:>6}'*7
    print(fs.format(*lis) + '\n' + str(get_DAG(sentence)))

if __name__ == '__main__':
    main()

