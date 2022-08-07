#!/usr/bin/env python
# coding: utf-8

# In[232]:


n = int(input())
a = list(map(int,input().split()))
b={}
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
for i,j in b.items():
    if j!=n:
        print(i)

