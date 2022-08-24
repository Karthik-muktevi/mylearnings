#!/usr/bin/env python
# coding: utf-8

# In[98]:


mean = 2.4
sd = 2
n = 100
target = 250
import math
def cdf(x,mean,sd):
    return 0.5*(1+math.erf((x-mean)/sd/2**(0.5)))

mean_p = n * mean
sd_p = sd * n**(0.5)
print(round(cdf(target,mean_p,sd_p),4))

