#!/usr/bin/env python
# coding: utf-8

# In[73]:


def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
def combination(n,x):
    return factorial(n)/(factorial(x)*factorial(n-x))
def binomial(x,n,p):
    return combination(n,x) * p**x * (1-p)**(n-x)
p, n = list(map(int, input().split(" ")))
print(round(sum([binomial(i,n,p/100) for i in range(3)]),3))
print(round(sum([binomial(i,n,p/100) for i in range(2,n+1)]),3))


# In[ ]:




