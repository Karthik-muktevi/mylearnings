#!/usr/bin/env python
# coding: utf-8

# In[ ]:




import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
matrix = list(zip(*matrix))

s = str()
for i in matrix:
    for j in i:
        s+=j
print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', s)) 

