#!/usr/bin/env python
# coding: utf-8

# In[34]:


a = int(input())
b = numpy.array([input().split() for i in range(a)],dtype=float)
c = numpy.linalg.det(b)
print(round(c,2))


# In[ ]:




