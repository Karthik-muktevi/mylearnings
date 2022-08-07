#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy

x,y = map(int,input().split())
a = numpy.array([input().split() for i in range(x)],dtype='int' )
b = numpy.array([input().split() for i in range(x)],dtype='int' )

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)


# In[ ]:




