#!/usr/bin/env python
# coding: utf-8

# In[253]:


import math

AB,BC=int(input()),int(input())

ang = round(math.degrees((math.atan2(AB,BC))))
degree=chr(176)                                
print(ang,degree, sep='')


# In[ ]:




