#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
def cdf(x,mean,sd):
    return 0.5*(1+math.erf((x-mean)/sd/2**(0.5)))

mean,sd = list(map(int,input().split()))
x1=float(input())
x2,x3=list(map(int,input().split()))
print(round(cdf(x1,mean,sd),3))
print(round(cdf(x3,mean,sd) - cdf(x2,mean,sd),3))

