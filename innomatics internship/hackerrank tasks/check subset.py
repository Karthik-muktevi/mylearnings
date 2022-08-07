#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())
for i in range(a):
    b = int(input())
    c = set(input().split())
    d = int(input())
    e = set(input().split())
    print(c.issubset(e))

