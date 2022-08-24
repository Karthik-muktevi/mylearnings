#!/usr/bin/env python
# coding: utf-8

# In[51]:


def factorial(n):
    return 1 if n == 0 else n*factorial(n-1)

def combination(n, x):
    return factorial(n) / (factorial(x) * factorial(n-x))

def binomial(x, n, p):
    return combination(n, x) * p**x * (1-p)**(n-x)

b,g = list(map(float, input().split(" ")))
ratio = b / g
print(round(sum([binomial(i, 6, ratio / (1 + ratio)) for i in range(3, 7)]), 3))


# In[ ]:




