#!/usr/bin/env python
# coding: utf-8

# In[10]:


import re

a = int(input())

for i in range(a):
    if re.match(r'^[7-9]\d{9}$',input()):
        print('YES')
    else:
        print('NO')


# In[ ]:




