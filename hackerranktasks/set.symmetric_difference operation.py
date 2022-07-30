#!/usr/bin/env python
# coding: utf-8

# In[226]:


a = int(input())
b = set(map(int,input().split()))
c = int(input())
d = set(map(int,input().split()))
print(len(b.symmetric_difference(d)))


# In[ ]:




