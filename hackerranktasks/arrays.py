#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr,dtype='f')
    return arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# In[ ]:




