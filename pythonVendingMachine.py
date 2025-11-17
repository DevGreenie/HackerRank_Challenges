#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price
    
    def buy(self, req_items, money):
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")
        
        
        total_cost = req_items * self.item_price
        if money < total_cost:
            raise ValueError("Not enough coins")
        
        self.num_items -= req_items
        return money - total_cost

    pass
if __name__ == '__main__':


# INPUT
# STDIN       Function
# -----       --------
# 10 2   →    num_items = 10, item_price = 2
# 4      →    n = 4
# 1 5    →    req_items = 1, money = 5       (1st transaction)
# 10 100 →    req_items = 10, money = 100    (2nd transaction)
# 7 100  →    req_items = 7, money = 100     (3rd transaction)
# 2 3    →    req_items = 2, money = 3       (4th transaction)

# 100 1
# 2
# 50 50
# 50 60