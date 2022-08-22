#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
a = int(input())

for i in range(a):
    
    regex = r'^[+-]?[0-9]*\.[0-9]+$'
    if(re.match(regex,input())): 
        print(True) 
          
    else: 
        print(False)


# In[ ]:




