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
    t0 = 'Sun 10 May 2015 13:54:36 -0700'
    t1 = 'Sun 10 May 2015 13:54:36 -0000'
    #Sat 02 May 2015 19:54:36 +0530
    #Fri 01 May 2015 13:54:36 -0000
    delta = time_delta(t1, t0)
    expected = (25200 , 88200)
