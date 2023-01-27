#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def get_r_c(s):
    s = s.replace(' ', '')
    if int(math.sqrt(len(s))) * int(math.sqrt(len(s))) == int(len(s)):
        return int(math.sqrt(len(s))) ,int(math.sqrt(len(s)))
    if int(math.sqrt(len(s))) * int(math.sqrt(len(s))) + 1 < len(s):
        return int(math.sqrt(len(s))) + 1, int(math.sqrt(len(s))) + 1
    else:
        return int(math.sqrt(len(s))), int(math.sqrt(len(s))) + 1

def encryption(s):
    r, c = get_r_c(s)
    z = 0
    s = s.replace(' ', '')
    data = []
    print('this is s : %s', s)
    for i in range(int(len(s) / c)):
        data.append(s[z:z+c])
        z = z + c
    if z < len(s):
        data.append(s[z:])
    i = 0
    res = ''
    while i <= c - 1:
        for x in data :
            if i < len(x):
                res += x[i]
            else:
                res += ''
        res += ' '
        i += 1
        
    print(res)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)
    print(result)

    fptr.write(result + '\n')

    fptr.close()
