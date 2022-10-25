#!/bin/python3

import math
import os
import random
import re
import sys
import time
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_date = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2_date = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    delta = abs(t1_date - t2_date)
    #t1_ts = datetime.timestamp(t1_date)
    #t2_ts = datetime.timestamp(t2_date)
    
    #if int(t1.split(' ')[1]) == int(t2.split(' ')[1]):
    #    return str(int(t1_ts - t2_ts))
    if delta.days >= 1:
        return str(24 * 3600 * delta.days + delta.seconds)
    return str(delta.seconds)
    
    
    

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
