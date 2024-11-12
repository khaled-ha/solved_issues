#!/bin/python3

import math
import os
import random
import re
import sys

symbols = ("!","@","#","$","%","&", " ")

def convert_matrix_tostr(matrix, n, m):
    alpha_sym_ids = []
    sentence  = ""
    for i in range(m):
        for j in range(n):
            sentence += str(matrix[j][i])
            alpha_sym_ids.append(1 if matrix[j][i] in symbols else 0)
    return sentence, alpha_sym_ids


def find_alpha_symbols(sentence):
    alpha_sym_ids = []
    for i in range(len(sentence)-1):
        alpha_sym_ids.append(1 if sentence[i] in symbols else 0)
    return alpha_sym_ids
    
def find_next_alpha(data):
    for i, v in enumerate(data):
        if v == 0:
            return i
    return i
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
sentence, symbols_ids = convert_matrix_tostr(matrix, n, m)
#symbols_ids = find_alpha_symbols(sentence)
#print(symbols_ids)
new_sentence = []
i = 0
while i < len(symbols_ids) - 1:
    if symbols_ids[i] == 1:
        next_alpha = find_next_alpha(symbols_ids[i+1:])
        if next_alpha < len(symbols_ids) -1:
            new_sentence.append(" ")
            i = next_alpha + 1
    else:
        new_sentence.append(sentence[i])
        
print(new_sentence)

