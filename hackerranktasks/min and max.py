#!/usr/bin/env python
# coding: utf-8

# In[29]:


import numpy

a,b = map(int,input().split())

c = numpy.array([input().split() for i in range(a)],dtype='int')

d= numpy.min(c,axis=1)
print(numpy.max(d))


# In[ ]:




