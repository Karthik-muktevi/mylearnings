#!/usr/bin/env python
# coding: utf-8

# In[117]:


import textwrap

def wrap(string, max_width):
    return ''.join(textwrap.fill(string,max_width))


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)


# In[ ]:




