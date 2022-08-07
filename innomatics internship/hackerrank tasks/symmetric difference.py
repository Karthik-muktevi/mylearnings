#!/usr/bin/env python
# coding: utf-8

# In[201]:


a = int(input())
b = set(map(int,input().split()))
c = int(input())
d = set(map(int,input().split()))
e = sorted(b.symmetric_difference(d))
for i in e:
    print(i)


# In[ ]:




