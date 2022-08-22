#!/usr/bin/env python
# coding: utf-8

# In[12]:


import re

a = int(input())
for i in range(a):
    b,c= input().split(' ')
    d =re.search(r'<[a-zA-Z][\w\.-]*@[a-zA-Z]*\.[a-zA-Z]{1,3}>', c)
    print(bool(d))
        
        


# In[ ]:




