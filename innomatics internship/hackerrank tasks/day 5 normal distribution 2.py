#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
def cdf(x,mean,sd):
    return 0.5*(1+math.erf((x-mean)/sd/2**(0.5)))

mean,sd = map(int,input().split())
x1= int(input())
x2 = int(input())

print(round(100-cdf(x1,mean,sd)*100,2))
print(round(100-cdf(x2,mean,sd)*100,2))  
print(round(cdf(x2,mean,sd)*100,2))

