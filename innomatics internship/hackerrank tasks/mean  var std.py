#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy

a,b = map(int,input().split())

c = numpy.array([input().split() for i in range(a)],dtype='int')

print(numpy.mean(c,axis=1))
print(numpy.var(c,axis=0))
print(numpy.std(c).round(11))


# In[ ]:




