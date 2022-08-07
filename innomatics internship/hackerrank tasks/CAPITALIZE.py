#!/usr/bin/env python
# coding: utf-8

# In[132]:


def solve(s):
    return ' '.join(x.capitalize() for x in s.split(" "))
s = input()
print(solve(s))


# In[ ]:




