#!/bin/python3

import math
import os
import random
import re
import sys



class ValueErrorException(ValueError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        

class VendingMachine:
    
    def __init__(self, num_items :int, item_price :float):
        self.num_items = num_items
        self.item_price = item_price
    
        
    def buy(self, req_items :int, money :float):
        if (req_items <= self.num_items) and (money >= req_items * self.item_price):
            self.num_items -= req_items
            return self.num_items
        if req_items > self.num_items:
            raise ValueErrorException('Not enought items in the machine')
        
        if req_items < self.num_items and not (money> req_items * self.item_price):
            raise ValueErrorException('Not enougth coins')

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
