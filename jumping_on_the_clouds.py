#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    position = 0
    while position <= len(c)-2:
        try:
            if c[position+2] == 0:
                position += 2
            else:
                position += 1
        except:
            position += 1
        print(f'pos: {position}')
        jumps += 1
    return jumps
