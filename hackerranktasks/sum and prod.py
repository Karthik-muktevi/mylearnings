#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy
a,b = map(int,input().split())

c = numpy.array([input().split() for i in range(a)],dtype='int')

d = numpy.sum(c,axis=0)
print(numpy.prod(d))


# In[ ]:




